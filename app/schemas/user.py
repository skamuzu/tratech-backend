from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

class UserRole(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    

class UserBase(BaseModel):
    id: UUID
    name: str
    email: EmailStr
    role: UserRole = UserRole.STUDENT
    image_url: Optional[str] = None
    joined_at: Optional[datetime] = None