from openpyxl import Workbook
from sqlalchemy.orm import Session
from app.db.models import Course
import io


class ExportService:
    def __init__(self, session: Session):
        self.db = session

    def get_courses_as_excel(self):
        courses = self.db.query(Course).all()

        wb = Workbook()
        ws = wb.active
        ws.title = "Courses"

        ws.append(["Course", "ID", "Status", "Total Lessons", "Total Modules", "Image"])

        for course in courses:
            ws.append(
                [
                    course.title,
                    str(course.id),
                    course.status,
                    course.total_lessons,
                    course.total_modules,
                    course.image,
                ]
            )

        stream = io.BytesIO()
        wb.save(stream)
                
        return stream