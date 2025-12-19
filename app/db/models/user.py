from app.db.database import Base
from datetime import datetime
from sqlalchemy import String, Enum as SQLEnum, Column, DateTime
from app.schemas.user import UserRole
from pytz import timezone


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    role = Column(SQLEnum(UserRole),default=UserRole.STUDENT)
    joined_at = Column(DateTime, default=lambda: datetime.now(tz=timezone("Africa/Accra"))) 
    image_url = Column(String, nullable=True)
