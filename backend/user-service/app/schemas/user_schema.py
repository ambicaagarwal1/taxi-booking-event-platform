from pydantic import BaseModel, EmailStr, Field, field_validator
import re

class UserCreate(BaseModel):

    name: str = Field(..., min_length=2, max_length=100)
    email: EmailStr

    phone: str = Field(..., pattern="^[0-9]{10}$")

    password: str = Field(..., min_length=8)

    @field_validator("password")
    def password_validator(cls, v):

        if not re.search(r"[A-Z]", v):
            raise ValueError("Password must contain one uppercase letter")

        if not re.search(r"[a-z]", v):
            raise ValueError("Password must contain one lowercase letter")

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            raise ValueError("Password must contain one special character")

        return v
