from app.db.database import Base
from datetime import datetime
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy import String, Enum as SQLEnum, Column, TIMESTAMP
from pytz import timezone


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    joined_at = Column(TIMESTAMP, default=lambda: datetime.now(tz=timezone("Africa/Accra"))) 
    image_url = Column(String, nullable=True)
