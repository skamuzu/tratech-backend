from pydantic import BaseModel
from typing import Optional
from uuid import UUID

class ModuleBase(BaseModel):
    title : str
    module_number: int

class ModuleCreate(ModuleBase):
    ...


class ModuleUpdate(BaseModel):
    title: Optional[str] = None
    module_number: Optional[str] = None


class ModuleRead(BaseModel):
    id: UUID
    title: str
    module_number: int = 1
    course_id: UUID
