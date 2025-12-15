from app.db.database import Base
from sqlalchemy import String, Enum as SQLEnum, TIMESTAMP
from sqlalchemy.orm import mapped_column, Mapped
from enum import Enum
from uuid import UUID


class UserRole(str, Enum):
    STUDENT = "Student"
    ADMIN = "Admin"


class User(Base):
    __tablename__ = "users"

    id: Mapped[UUID] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String(30), nullable=False, unique=True)
    role: Mapped[str] = mapped_column(
        SQLEnum(UserRole, name="user_role"), nullable=False, default=UserRole.STUDENT
    )
