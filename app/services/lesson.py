from sqlalchemy.orm import Session
from app.schemas.lesson import LessonCreate, LessonUpdate
from app.db.models import Lesson
from typing import List
from fastapi import Depends
from app.core.dependencies import get_db

def get_lesson_service(db: Session = Depends(get_db)):
    return LessonService(session=db)
class LessonService:
    def __init__(self, session: Session):
        self.db = session

    def create_lesson(self, data: LessonCreate) -> Lesson:
        lesson = Lesson(
            title=data.title,
            lesson_number=data.lesson_number,
            content=data.content,
            module_id=data.module_id
        )

        self.db.add(lesson)
        self.db.commit()
        self.db.refresh(lesson)

        return lesson

    def update_lesson(self, lesson_id: str, data: LessonUpdate) -> Lesson:
        lesson = self.db.query(Lesson).filter(Lesson.id == lesson_id).first()
        if not lesson:
            raise ValueError("Lesson not found")

        # Update fields only if provided
        if data.title is not None:
            lesson.title = data.title
        if data.lesson_number is not None:
            lesson.lesson_number = data.lesson_number
        if data.content is not None:
            lesson.content = data.content

        self.db.commit()
        self.db.refresh(lesson)
        return lesson

    def delete_lesson(self, lesson_id: str) -> Lesson:
        lesson = self.db.query(Lesson).filter(Lesson.id == lesson_id).first()
        if not lesson:
            raise ValueError("Lesson not found")
        
        self.db.delete(lesson)
        self.db.commit()
        return lesson

    def get_lesson(self, lesson_id: str) -> Lesson:
        lesson = self.db.query(Lesson).filter(Lesson.id == lesson_id).first()
        return lesson

    def get_all_lessons(self, module_id: str = None) -> List[Lesson]:
        query = self.db.query(Lesson)
        if module_id:
            query = query.filter(Lesson.module_id == module_id)
        lessons = query.order_by(Lesson.lesson_number).all()
        return lessons

    def count_lessons(self, module_id: str = None) -> int:
        query = self.db.query(Lesson)
        if module_id:
            query = query.filter(Lesson.module_id == module_id)
        count = query.count()
        return count

    