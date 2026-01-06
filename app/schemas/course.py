from pydantic import BaseModel
from typing import Optional
from enum import Enum
from uuid import UUID


class Status(str, Enum):
    DRAFT = "draft"
    PUBLISHED = "published"


class CourseBase(BaseModel):
    title: str
    subtitle: Optional[str] = None
    image: Optional[str] = None
    status: Status = Status.DRAFT
  
    
class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    subtitle: Optional[str] = None
    image: Optional[str] = None
    status: Optional[Status] = None
    


class CourseRead(CourseBase):
    id: UUID
    title: str
    subtitle: Optional[str]
    image: Optional[str]
    status: Status
    slug: str
    total_lessons: int = 0
    total_modules: int = 0

    class Config:
        from_attributes = True
