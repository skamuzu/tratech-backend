from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserRole(str, Enum):
    ADMIN = "admin"
    STUDENT = "student"
    

class UserBase(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: UserRole 
    image_url: Optional[str] = None
    joined_at: Optional[datetime] = None
    
