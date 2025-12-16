from sqlalchemy.orm import Session
from app.schemas.user import UserCreate
from app.db.models.user import User


class UserService:
    def __init__(self, session: Session):
        self.db = session

    def create_user(self, user_data: UserCreate) -> User:
        with self.db.begin():
            new_user = User(
                id=user_data.id,
                name=user_data.name,
                email=user_data.email,
                role=user_data.role,
            )
            self.db.add(new_user)
        return new_user
