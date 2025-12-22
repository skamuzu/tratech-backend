from app.db.database import Base
from sqlalchemy import Column, Uuid, String, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from uuid import uuid4

class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(Uuid, primary_key=True, default=lambda: uuid4())
    title = Column(String, nullable=False)
    lesson_number = Column(Integer, nullable=False)
    module_id = Column(Uuid, ForeignKey("modules.id", ondelete="CASCADE"))
    content = Column(Text)
    
    module = relationship("Module", back_populates="lessons")