from pydantic import BaseModel
from typing import Optional, List
from uuid import UUID


class ModuleBase(BaseModel):
    title: str
    module_number: int


class ModuleCreate(ModuleBase):
    course_id: UUID


class ModuleUpdate(BaseModel):
    title: Optional[str] = None
    module_number: Optional[int] = None


class ModuleRead(ModuleBase):
    id: UUID
    course_id: UUID
    total_lessons: int = 0

    class Config:
        from_attributes = True
