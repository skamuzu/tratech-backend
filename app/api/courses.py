from fastapi import APIRouter, Depends, Form, File, UploadFile
from fastapi.responses import StreamingResponse
from app.core.dependencies import get_db
from app.services.course import CourseService
from app.services.file_exports import ExportService
from app.schemas.course import CourseCreate, CourseRead, CourseUpdate
from app.schemas.module import ModuleRead
from typing import List
from uuid import UUID
from app.utils.image_upload import upload_image


def get_course_service(db=Depends(get_db)):
    return CourseService(session=db)


def get_export_service(db=Depends(get_db)):
    return ExportService(session=db)


router = APIRouter(prefix="/courses")


@router.post("/", response_model=CourseRead)
async def create_course(
    title: str = Form(...),
    subtitle: str | None = Form(None),
    status: str = Form("draft"),
    image: UploadFile | None = File(None),
    course_service: CourseService = Depends(get_course_service),
):
    image_url = None

    if image:
        image_url = await upload_image(image=image)

    course_data = CourseCreate(
        title=title, subtitle=subtitle, status=status, image=image_url
    )

    course = course_service.create_course(data=course_data)
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
def get_course(
    course_id: UUID, course_service: CourseService = Depends(get_course_service)
):
    course = course_service.get_course(course_id)
    return course


@router.delete("/{course_id}", response_model=CourseRead)
def delete_course(
    course_id: UUID, course_service: CourseService = Depends(get_course_service)
):
    course = course_service.delete_course(course_id)
    return course


@router.get("/{course_id}/modules", response_model=List[ModuleRead])
def get_course_modules(
    course_id: UUID, course_service: CourseService = Depends(get_course_service)
):
    modules = course_service.get_course_modules(course_id)
    return modules


@router.get("/excel/download")
def get_course_as_excel(export_service: ExportService = Depends(get_export_service)):
    stream = export_service.get_courses_as_excel()
    stream.seek(0)

    headers = {"Content-Disposition": "attachment"}

    return StreamingResponse(
        stream,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers=headers
    )