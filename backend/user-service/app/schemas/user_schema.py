from pydantic import BaseModel
from typing import Optional

class UserRegister(BaseModel):
    name: str
    phone: str
    password: str
    email: Optional[str] = None