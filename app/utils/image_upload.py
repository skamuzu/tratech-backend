import cloudinary
from cloudinary.uploader import upload
from fastapi import UploadFile, status, HTTPException
from app.core.config import settings


cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_SECRET_KEY
)

async def upload_image(image: UploadFile):
    try:
        upload_result= upload(image.file)
        file_url =upload_result['secure_url']
        return file_url
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=f"Error uploading images: {e}")
        