from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.database.db import get_db_connection
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

@app.get("/")
def read_root():
    return {
        "message": "User Service Running",
        "version": settings.APP_VERSION,
        "service": settings.APP_NAME
    }

@app.get("/test-db")
def test_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT version();")
    result = cursor.fetchone()
    conn.close()

    return {"postgres_version": result}

app.include_router(user_router)
