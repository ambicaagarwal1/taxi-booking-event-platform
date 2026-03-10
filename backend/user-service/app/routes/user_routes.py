from fastapi import APIRouter
from app.schemas.user_schema import UserRegister
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/users/register")
def register_user(user: UserRegister):

    user_id = str(uuid.uuid4())
    created_at = datetime.utcnow()

    return {
        "user_id": user_id,
        "name": user.name,
        "phone": user.phone,
        "email": user.email,
        "created_at": created_at,
        "message": "User registered successfully"
    }