from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserCreate
from app.database.db import get_db_connection
import uuid
import bcrypt
import psycopg2

router = APIRouter()

@router.post("/users/register")
def register_user(user: UserCreate):
    """
    Register a new user.
    
    This endpoint:
    1. Validates input data (handled by Pydantic schema)
    2. Generates a unique UUID for the user
    3. Hashes the password using bcrypt
    4. Stores user in PostgreSQL database
    5. Returns user_id on success
    
    Error Handling:
    - 409: Phone number already exists (duplicate)
    - 500: Database connection or other server errors
    """
    conn = None
    cursor = None
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        user_id = str(uuid.uuid4())

        # Hash password using bcrypt (industry standard)
        # bcrypt automatically handles salt generation
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

        return {
            "message": "User created successfully",
            "user_id": user_id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone
        }
    
    except psycopg2.errors.UniqueViolation:
        # Handle duplicate phone number
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=409,
            detail=f"Phone number {user.phone} is already registered"
        )
    
    except psycopg2.Error as db_error:
        # Handle other database errors
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Database error: {str(db_error)}"
        )
    
    except Exception as e:
        # Handle unexpected errors
        if conn:
            conn.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Internal server error: {str(e)}"
        )
    
    finally:
        # Always close database connections
        if cursor:
            cursor.close()
        if conn:
            conn.close()
