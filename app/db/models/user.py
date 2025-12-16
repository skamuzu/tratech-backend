from app.db.database import Base
from datetime import datetime
from sqlalchemy import VARCHAR, Enum as SQLEnum, Column, DATETIME
from app.schemas.user import UserRole
from pytz import timezone


class User(Base):
    __tablename__ = "users"

    id = Column(VARCHAR(20), primary_key=True)
    name = Column(VARCHAR(50))
    email = Column(VARCHAR(20), unique=True)
    role = Column(SQLEnum(UserRole),default=UserRole.STUDENT)
    joined_at = Column(DATETIME, default=lambda: datetime.now(tz=timezone("Africa/Accra"))) 

