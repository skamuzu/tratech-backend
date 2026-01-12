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
        user = self.db.query(User).filter_by(id=clerk_user["id"]).first()
        if user:
            return user

        public_metadata = clerk_user.get("public_metadata") or {}
        role = public_metadata.get("role", UserRole.STUDENT.value)

        if "role" not in public_metadata:
            sdk.users.update_metadata(user_id=clerk_user["id"], public_metadata={"role": role})

        email_addresses = clerk_user.get("email_addresses", [])
        if not email_addresses:
            raise ValueError("Clerk user has no email")

        primary_email_id = clerk_user["primary_email_address_id"]
        email = next(
            e["email_address"] for e in email_addresses if e["id"] == primary_email_id
        )

        user = User(
            id=clerk_user["id"],
            email=email,
            name=f"{clerk_user.get('first_name')} {clerk_user.get('last_name')}",
            image_url=clerk_user.get("image_url"),
        )

        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
        except:
            self.db.rollback()
            raise

        return user

    def count_users(self) -> int:
        count = self.db.query(User).count()
        return count

    def clerk_email_invites(self, invitations: list[InviteItem]):
        request_payload = [invite.model_dump(mode="json") for invite in invitations]
        res = sdk.invitations.bulk_create(request=request_payload)
        return res
