from app.db.database import Base
from sqlalchemy import Column, Uuid, String, TEXT, Enum as SQLEnum, Integer, DateTime
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime
from pytz import timezone
from app.schemas.course import Status


class Course(Base):

    __tablename__ = "courses"

    id = Column(Uuid, primary_key=True, default=lambda: uuid4())
    title = Column(String, nullable=False)
    subtitle = Column(String)
    slug = Column(String, nullable=False, unique=True)
    status = Column(SQLEnum(Status, name="course_status"), default=Status.DRAFT)
    total_lessons = Column(Integer)
    created_at = Column(
        DateTime, default=lambda: datetime.now(tz=timezone("Africa/Accra"))
    )
    image = Column(String)

    modules = relationship(
        "Module",
        back_populates="course",
        cascade="all, delete-orphan",
    )
