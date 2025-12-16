from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent 


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8",case_sensitive=True)

    CLERK_BACKEND_API_URL: str
    CLERK_SECRET_KEY: str
    CLERK_FRONTEND_API_URL: str
    DATABASE_URL: str


@lru_cache
def get_settings():
    return Settings()

settings = get_settings()

