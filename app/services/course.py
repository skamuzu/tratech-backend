from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate

class CourseService:
    def __init__(self, session: Session):
        self.db = session
    
