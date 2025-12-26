from fastapi import FastAPI
from app.api import users, courses
from app.core.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    settings.CLERK_FRONTEND_API_URL
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(courses.router)

@app.api_route("/health", include_in_schema=False, methods=["GET","HEAD"])
def health_check():
    return {"status": "ok"}

