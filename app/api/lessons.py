from fastapi import APIRouter, Depends, Query
from app.core.dependencies import get_db
from app.services.lesson import LessonService
from app.schemas.lesson import LessonCreate, LessonRead, LessonUpdate
from typing import List, Optional
from uuid import UUID


def get_lesson_service(db=Depends(get_db)):
    return LessonService(session=db)


router = APIRouter(prefix="/lessons")


@router.post("/", response_model=LessonRead)
def create_lesson(
    lesson: LessonCreate, lesson_service: LessonService = Depends(get_lesson_service)
):
    lesson = lesson_service.create_lesson(data=lesson)
    return lesson


@router.get("/", response_model=List[LessonRead])
def get_all_lessons(
    module_id: Optional[UUID] = Query(None),
    lesson_service: LessonService = Depends(get_lesson_service)
):
    lessons = lesson_service.get_all_lessons(module_id=module_id)
    return lessons


@router.patch("/{lesson_id}", response_model=LessonRead)
def update_lesson(
    lesson_id: UUID,
    lesson: LessonUpdate,
    lesson_service: LessonService = Depends(get_lesson_service),
):
    lesson = lesson_service.update_lesson(lesson_id, lesson)
    return lesson


@router.get("/{lesson_id}", response_model=LessonRead)
def get_lesson(
    lesson_id: UUID, lesson_service: LessonService = Depends(get_lesson_service)
):
    lesson = lesson_service.get_lesson(lesson_id)
    return lesson


@router.delete("/{lesson_id}", response_model=LessonRead)
def delete_lesson(
    lesson_id: UUID, lesson_service: LessonService = Depends(get_lesson_service)
):
    lesson = lesson_service.delete_lesson(lesson_id)
    return lesson
