from fastapi import APIRouter, Depends
from app.core.dependencies import get_db
from app.services.course import CourseService
from app.schemas.course import CourseCreate, CourseRead, CourseUpdate
from typing import List
from uuid import UUID


def get_course_service(db=Depends(get_db)):
    return CourseService(session=db)


router = APIRouter(prefix="/courses")


@router.post("/", response_model=CourseRead)
def create_course(
    course: CourseCreate, course_service: CourseService = Depends(get_course_service)
):
    course = course_service.create_course(data=course)
    return course


@router.get("/", response_model=List[CourseRead])
def get_all_courses(course_service: CourseService = Depends(get_course_service)):
    courses = course_service.get_all_courses()
    return courses


@router.patch("/{course_id}", response_model=CourseRead)
def update_course(
    course_id: UUID,
    course: CourseUpdate,
    course_service: CourseService = Depends(get_course_service),
):
    course = course_service.update_course(course_id, course)
    return course

@router.get("/{course_id}", response_model=CourseRead)
def get_course(course_id: UUID, course_service: CourseService = Depends(get_course_service)):
    course = course_service.get_course(course_id)
    return course

@router.delete("/{course_id}", response_model=CourseRead)
def delete_course(course_id: UUID, course_service: CourseService = Depends(get_course_service)):
    course = course_service.delete_course(course_id)
    return course
