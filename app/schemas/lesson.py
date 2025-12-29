from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class LessonBase(BaseModel):
    title: str
    lesson_number: int
    content: Optional[str] = None


class LessonCreate(LessonBase):
    module_id: UUID


class LessonUpdate(BaseModel):
    title: Optional[str] = None
    lesson_number: Optional[int] = None
    content: Optional[str] = None


class LessonRead(LessonBase):
    id: UUID
    module_id: UUID

    class Config:
        from_attributes = True
