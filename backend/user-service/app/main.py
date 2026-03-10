from fastapi import FastAPI
from app.routes.user_routes import router as user_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "User Service Running"}

app.include_router(user_router)