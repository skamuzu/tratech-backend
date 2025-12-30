from sqlalchemy.orm import Session
from app.schemas.user import UserRole
from app.db.models.user import User
from app.core.dependencies import get_db
from fastapi import Depends

def get_user_service(db: Session = Depends(get_db)):
    return UserService(db)
class UserService:
    def __init__(self, session: Session):
        self.db = session

    def create_user_from_clerk(self, clerk_user: dict) -> User:
        user = self.db.query(User).filter(User.id == clerk_user["id"]).first()
        
        if user:
            return user
        
        if len(clerk_user["email_addresses"]) == 0:
            email = "johndoe@gmail.com"
        else:
            email = clerk_user["email_addresses"][0]["email_address"]
        

        user = User(
            id=clerk_user["id"],
            email=email,
            name=f"{clerk_user.get("first_name")} {clerk_user.get("last_name")}",
            role=UserRole.STUDENT,
            image_url=clerk_user.get("image_url")
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        return user
    
    def count_users(self) -> int:
        count = self.db.query(User).count()
        return count