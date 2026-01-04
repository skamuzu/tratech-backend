from sqlalchemy.orm import Session
from app.db.models.user import User
from app.schemas.user import UserRole
from app.schemas.invites import InviteItem
from app.core.dependencies import get_db
from fastapi import Depends
from app.core.auth import sdk


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
            return 

        user = User(
            id=clerk_user["id"],
            email=clerk_user["email_addresses"][0]["email_address"],
            name=f"{clerk_user.get("first_name")} {clerk_user.get("last_name")}",
            role=UserRole.STUDENT.value,
            image_url=clerk_user.get("image_url"),
        )

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)

        try:
            user = sdk.users.get(clerk_user["id"])
            if user.public_metadata.get("role") == None:
                sdk.users.update_metadata(
                    user_id=clerk_user["id"],
                    public_metadata={"role": UserRole.STUDENT},
                )
                
            
            print(f"✅ Updated metadata for new user {user.id}")
        except Exception as e:
            print(f"❌ Failed to update metadata: {e}")

        return user

    def count_users(self) -> int:
        count = self.db.query(User).count()
        return count

    def clerk_email_invites(self, invitations: list[InviteItem]):
        request_payload = [invite.model_dump(mode='json') for invite in invitations]
        res = sdk.invitations.bulk_create(request=request_payload)
        return res