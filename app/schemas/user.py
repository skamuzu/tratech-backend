from enum import Enum
from pydantic import BaseModel, EmailStr
from typing import Optional

class UserRole(str, Enum):
    ADMIN = "Admin"
    STUDENT = "Student"
    

  