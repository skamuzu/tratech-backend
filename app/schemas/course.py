# class Course(Base):

#     __tablename__ = "courses"

#     id = Column(Uuid, primary_key=True, default=lambda: uuid4())
#     title = Column(String, nullable=False)
#     subtitle = Column(String)
#     slug = Column(String, nullable=False, unique=True)
#     status = Column(SQLEnum(Status), default=Status.DRAFT)
#     total_lessons = Column(Integer)
#     created_at = Column(
#         DateTime, default=lambda: datetime.now(tz=timezone("Africa/Accra"))
#     )
#     image = Column(String)
    
#     module = relationship("Module", back_populates="course")

from pydantic import BaseModel
from typing import Optional
from enum import Enum



class Status(str, Enum):
    DRAFT = "Draft"
    PUBLISHED = "Published"

class CourseCreate(BaseModel):
    title : str
    subtitle : Optional[str]
    status: Optional[Status]
    image: Optional[str]
