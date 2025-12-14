from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from core.config import Settings
from functools import lru_cache


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@lru_cache
def get_settings():
    return Settings()

