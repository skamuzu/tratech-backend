from pydantic import BaseModel, EmailStr, HttpUrl, ConfigDict
from .user import UserRole


class MetaData(BaseModel):
    role: UserRole


class InviteItem(BaseModel):

    model_config = ConfigDict(arbitrary_types_allowed=True)

    email_address: EmailStr
    public_metadata: MetaData
    redirect_url: HttpUrl
    expires_in_days: int
    notify: bool = True
    ignore_existing: bool = True
