from app.db.database import Base
from sqlalchemy import Column, Uuid, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from uuid import uuid4


class Module(Base):

    __tablename__ = "modules"

    id = Column(Uuid, primary_key=True, default=lambda: uuid4())
    title = Column(String, nullable=False)
    module_number = Column(Integer, nullable=False)
    course_id = Column(
        Uuid, ForeignKey("courses.id", ondelete="CASCADE"), nullable=False
    )

    course = relationship("Course", back_populates="modules")
    lessons = relationship("Lesson", back_populates="modules", cascade="all, delete-orphan")
