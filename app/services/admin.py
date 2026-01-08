from .course import get_course_service
from .lesson import get_lesson_service
from .user import get_user_service
from fastapi import Depends

def get_dashboard_service(
    user_service=Depends(get_user_service),
    course_service=Depends(get_course_service),
    lesson_service=Depends(get_lesson_service),
):
    return DashboardService(
        user_service=user_service,
        course_service=course_service,
        lesson_service=lesson_service,
    )


class DashboardService:
    def __init__(
        self,
        user_service,
        course_service,
        lesson_service,
    ):
        self.user_service = user_service
        self.course_service = course_service
        self.lesson_service = lesson_service

    def get_dashboard_data(self):
        return {
            "number_of_users": self.user_service.count_users(),
            "number_of_courses": self.course_service.count_courses(),
            "number_of_lessons": self.lesson_service.count_lessons(),
            "courses": self.course_service.get_all_courses(),
            "number_of_published_courses": self.course_service.get_number_of_published_courses(),
        }

