from fastapi import FastAPI
from fastapi.responses import JSONResponse
from app.routes.user_routes import router as user_router
from app.database.db import get_db_connection
from app.config import settings
import time

# Record when the application started
# Used to calculate uptime in health check
START_TIME = time.time()

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)


@app.get("/")
def read_root():
    """
    Root endpoint - Quick info about the service.
    
    Use this to verify the service is reachable.
    """
    return {
        "message": "User Service Running",
        "version": settings.APP_VERSION,
        "service": settings.APP_NAME
    }


@app.get("/health")
def health_check():
    """
    Health Check Endpoint.
    
    Checks:
    1. Is the application running? (if you get a response, yes!)
    2. Is the database connected? (tries a simple query)
    3. How long has the service been running? (uptime)
    
    Returns:
        - 200 with status "healthy" if everything is OK
        - 503 with status "unhealthy" if database is down
    
    Used by:
        - Docker health checks
        - Kubernetes liveness/readiness probes
        - Load balancers
        - Monitoring tools (Prometheus, Grafana)
    """
    uptime = round(time.time() - START_TIME, 2)
    
    # Check database connectivity
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT 1")  # Simplest possible query
        cursor.close()
        conn.close()
        db_status = "connected"
        db_healthy = True
    except Exception as e:
        db_status = "disconnected"
        db_healthy = False
    
    # Build response
    health_data = {
        "status": "healthy" if db_healthy else "unhealthy",
        "service": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "database": db_status,
        "uptime_seconds": uptime
    }
    
    # Return 200 if healthy, 503 if unhealthy
    if db_healthy:
        return health_data
    else:
        return JSONResponse(status_code=503, content=health_data)


app.include_router(user_router)
