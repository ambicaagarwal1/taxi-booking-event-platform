from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import ClassVar
import re

class UserCreate(BaseModel):
    """
    User registration schema with comprehensive validation.
    
    Validates:
    - Name: 2-100 characters
    - Email: Valid email format
    - Phone: Exactly 10 digits
    - Password: Minimum 8 characters with complexity requirements
    """
    
    name: str = Field(
        ..., 
        min_length=2, 
        max_length=100,
        description="User's full name",
        examples=["John Doe"]
    )
    
    email: EmailStr = Field(
        ...,
        description="Valid email address",
        examples=["john.doe@example.com"]
    )
    
    phone: str = Field(
        ..., 
        pattern="^[0-9]{10}$",
        description="10-digit phone number",
        examples=["9876543210"]
    )
    
    password: str = Field(
        ..., 
        min_length=8,
        description="Password with minimum 8 characters, including uppercase, lowercase, digit, and special character",
        examples=["SecurePass@123"]
    )
    
    # Password validation error messages
    PASSWORD_MIN_LENGTH: ClassVar[int] = 8
    PASSWORD_ERRORS: ClassVar[dict] = {
        "min_length": f"Password must be at least {PASSWORD_MIN_LENGTH} characters long",
        "uppercase": "Password must contain at least one uppercase letter (A-Z)",
        "lowercase": "Password must contain at least one lowercase letter (a-z)",
        "digit": "Password must contain at least one digit (0-9)",
        "special": "Password must contain at least one special character (!@#$%^&*(),.?\":{}|<>)"
    }

    @field_validator("password")
    def password_validator(cls, v):
        """
        Validates password complexity requirements.
        
        Requirements:
        1. Minimum 8 characters (handled by Field min_length)
        2. At least one uppercase letter
        3. At least one lowercase letter
        4. At least one digit
        5. At least one special character
        
        Args:
            v: Password string to validate
            
        Returns:
            str: Validated password
            
        Raises:
            ValueError: If password doesn't meet requirements
        """
        errors = []
        
        # Check for uppercase letter
        if not re.search(r"[A-Z]", v):
            errors.append(cls.PASSWORD_ERRORS["uppercase"])
        
        # Check for lowercase letter
        if not re.search(r"[a-z]", v):
            errors.append(cls.PASSWORD_ERRORS["lowercase"])
        
        # Check for digit
        if not re.search(r"[0-9]", v):
            errors.append(cls.PASSWORD_ERRORS["digit"])
        
        # Check for special character
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", v):
            errors.append(cls.PASSWORD_ERRORS["special"])
        
        # If there are validation errors, raise them all at once
        if errors:
            raise ValueError(". ".join(errors))
        
        return v
    
    @field_validator("phone")
    def phone_validator(cls, v):
        """
        Additional phone validation beyond regex pattern.
        
        Args:
            v: Phone number string
            
        Returns:
            str: Validated phone number
            
        Raises:
            ValueError: If phone format is invalid
        """
        # Remove any spaces or dashes if present
        cleaned_phone = v.replace(" ", "").replace("-", "")
        
        # Check if exactly 10 digits
        if not cleaned_phone.isdigit():
            raise ValueError("Phone number must contain only digits")
        
        if len(cleaned_phone) != 10:
            raise ValueError("Phone number must be exactly 10 digits")
        
        # Check if phone doesn't start with 0 or 1 (Indian phone numbers)
        if cleaned_phone[0] in ['0', '1']:
            raise ValueError("Phone number cannot start with 0 or 1")
        
        return cleaned_phone
    
    @field_validator("name")
    def name_validator(cls, v):
        """
        Validates name format.
        
        Args:
            v: Name string
            
        Returns:
            str: Validated and cleaned name
            
        Raises:
            ValueError: If name format is invalid
        """
        # Remove extra whitespace
        cleaned_name = " ".join(v.split())
        
        # Check if name contains only letters and spaces
        if not re.match(r"^[a-zA-Z\s]+$", cleaned_name):
            raise ValueError("Name must contain only letters and spaces")
        
        return cleaned_name
