from fastapi import APIRouter, Depends, Query
from app.core.dependencies import get_db
from app.services.module import ModuleService
from app.schemas.module import ModuleCreate, ModuleRead, ModuleUpdate
from typing import List, Optional
from uuid import UUID


def get_module_service(db=Depends(get_db)):
    return ModuleService(session=db)


router = APIRouter(prefix="/modules")


@router.post("/", response_model=ModuleRead)
def create_module(
    module: ModuleCreate, module_service: ModuleService = Depends(get_module_service)
):
    module = module_service.create_module(data=module)
    return module


@router.get("/", response_model=List[ModuleRead])
def get_all_modules(
    course_id: Optional[UUID] = Query(None),
    module_service: ModuleService = Depends(get_module_service)
):
    modules = module_service.get_all_modules(course_id=course_id)
    return modules


@router.patch("/{module_id}", response_model=ModuleRead)
def update_module(
    module_id: UUID,
    module: ModuleUpdate,
    module_service: ModuleService = Depends(get_module_service),
):
    module = module_service.update_module(module_id, module)
    return module


@router.get("/{module_id}", response_model=ModuleRead)
def get_module(
    module_id: UUID, module_service: ModuleService = Depends(get_module_service)
):
    module = module_service.get_module(module_id)
    return module


@router.delete("/{module_id}", response_model=ModuleRead)
def delete_module(
    module_id: UUID, module_service: ModuleService = Depends(get_module_service)
):
    module = module_service.delete_module(module_id)
    return module
