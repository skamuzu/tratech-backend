from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseUpdate
from app.db.models import Course
from slugify import slugify
from typing import List

class CourseService:
    def __init__(self, session: Session):
        self.db = session

    def create_course(self, data: CourseCreate) -> Course:
        base_slug = slugify(data.title)
        slug = base_slug
        counter = 1

        while self.db.query(Course).filter(Course.slug == slug).first() is not None:
            slug = f"{base_slug}-{counter}"
            counter += 1

        course = Course(
            title=data.title,
            subtitle=data.subtitle,
            image=data.image,
            status=data.status,
            slug=slug
        )

        self.db.add(course)
        self.db.commit()
        self.db.refresh(course)

        return course

    def update_course(self, course_id: str, data: CourseUpdate) -> Course:
        course = self.db.query(Course).filter(Course.id == course_id).first()
        if not course:
            raise ValueError("Course not found")  # Or custom HTTPException in API

        # Update fields only if provided
        if data.title is not None:
            course.title = data.title
            # Update slug safely
            base_slug = slugify(data.title)
            slug = base_slug
            counter = 1
            while (
                self.db.query(Course)
                .filter(Course.slug == slug, Course.id != course.id)
                .first()
            ):
                slug = f"{base_slug}-{counter}"
                counter += 1
            course.slug = slug

        if data.subtitle is not None:
            course.subtitle = data.subtitle
        if data.image is not None:
            course.image = data.image
        if data.status is not None:
            course.status = data.status

        self.db.commit()
        self.db.refresh(course)
        return course

    def delete_course(self, course_id: str) -> Course:
        course = self.db.query(Course).filter(Course.id == course_id).first()
        self.db.delete(course)
        self.db.commit()
        return course

    def get_course(self, course_id: str) -> Course:
        course = self.db.query(Course).filter(Course.id == course_id).first()
        return course

    def get_all_courses(self) -> List[Course]:
        courses = self.db.query(Course).all()
        return courses

    def count_courses(self) -> int:
        count = self.db.query(Course).count()
        return count
