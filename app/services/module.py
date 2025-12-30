from sqlalchemy.orm import Session
from app.schemas.module import ModuleCreate, ModuleUpdate
from app.db.models import Module
from typing import List
from fastapi import Depends
from app.core.dependencies import get_db

def get_module_service(db: Session = Depends(get_db)):
    return ModuleService(session=db)
class ModuleService:
    def __init__(self, session: Session):
        self.db = session

    def create_module(self, data: ModuleCreate) -> Module:
        module = Module(
            title=data.title,
            module_number=data.module_number,
            course_id=data.course_id
        )

        self.db.add(module)
        self.db.commit()
        self.db.refresh(module)

        return module

    def update_module(self, module_id: str, data: ModuleUpdate) -> Module:
        module = self.db.query(Module).filter(Module.id == module_id).first()
        if not module:
            raise ValueError("Module not found")

        # Update fields only if provided
        if data.title is not None:
            module.title = data.title
        if data.module_number is not None:
            module.module_number = data.module_number

        self.db.commit()
        self.db.refresh(module)
        return module

    def delete_module(self, module_id: str) -> Module:
        module = self.db.query(Module).filter(Module.id == module_id).first()
        if not module:
            raise ValueError("Module not found")
        
        self.db.delete(module)
        self.db.commit()
        return module

    def get_module(self, module_id: str) -> Module:
        module = self.db.query(Module).filter(Module.id == module_id).first()
        return module

    def get_all_modules(self, course_id: str = None) -> List[Module]:
        query = self.db.query(Module)
        if course_id:
            query = query.filter(Module.course_id == course_id)
        modules = query.order_by(Module.module_number).all()
        return modules

    def count_modules(self, course_id: str = None) -> int:
        query = self.db.query(Module)
        if course_id:
            query = query.filter(Module.course_id == course_id)
        count = query.count()
        return count
