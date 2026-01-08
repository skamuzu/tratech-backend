from pydantic import BaseModel
from .course import CourseRead
from typing import List

class DashboardData(BaseModel):
    number_of_users: int
    number_of_courses: int
    number_of_lessons: int
    courses: List[CourseRead]
    number_of_published_courses: int