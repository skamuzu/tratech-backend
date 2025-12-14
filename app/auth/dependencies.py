from clerk_backend_api import Clerk
from clerk_backend_api.security import authenticate_request
from clerk_backend_api.security.types import AuthenticateRequestOptions
from fastapi import Request
from ..dependencies import get_settings

settings = get_settings()

clerk_sdk = Clerk(
    AuthenticateRequestOptions(
        authorized_parties=["http://localhost:3000", settings.CLERK_FRONTEND_API_URL]
    ),
    bearer_auth=settings.CLERK_SECRET_KEY,
)

def is_signed_in(request: Request):
    request_state = clerk_sdk.authenticate_request(request)
    return request_state.is_signed_in
