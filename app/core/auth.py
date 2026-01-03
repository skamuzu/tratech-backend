from clerk_backend_api import Clerk
from .config import settings


sdk = Clerk(
    bearer_auth=settings.CLERK_SECRET_KEY,
)

