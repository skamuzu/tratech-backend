from sqlalchemy.orm import Session
from app.db.database import sessionLocal
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()