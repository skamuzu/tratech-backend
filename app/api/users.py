from fastapi import APIRouter, Request, Response, status, Depends, HTTPException
from svix.webhooks import Webhook, WebhookVerificationError
from app.services.user import UserService
from app.core.config import settings
from app.core.dependencies import get_db


def get_user_service(db=Depends(get_db)) -> UserService:
    return UserService(session=db)


router = APIRouter(prefix="/users")


@router.post("/webhooks/clerk")
async def clerk_webhook(
    request: Request,
    user_service: UserService = Depends(get_user_service),
):
    payload = await request.body()
    headers = dict(request.headers)

    try:
        wh = Webhook(settings.CLERK_WEBHOOK_SECRET)
        event = wh.verify(payload, headers)
    except WebhookVerificationError:
        raise HTTPException(status_code=400, detail="Invalid webhook")

    if event["type"] == "user.created":
        user_service.create_user_from_clerk(event["data"])

    return {"status": "ok"}
