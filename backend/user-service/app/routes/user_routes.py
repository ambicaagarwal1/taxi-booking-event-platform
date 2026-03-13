from fastapi import APIRouter
from app.schemas.user_schema import UserCreate
from app.database.db import get_db_connection
import uuid
import bcrypt

router = APIRouter()

@router.post("/users/register")
def register_user(user: UserCreate):

    conn = get_db_connection()
    cursor = conn.cursor()

    user_id = str(uuid.uuid4())

    # Hash password
    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"),
        bcrypt.gensalt()
    ).decode("utf-8")

    query = """
    INSERT INTO users (id, name, email, phone, password)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(query, (
        user_id,
        user.name,
        user.email,
        user.phone,
        hashed_password
    ))

    conn.commit()

    cursor.close()
    conn.close()

    return {
        "message": "User created successfully",
        "user_id": user_id
    }
