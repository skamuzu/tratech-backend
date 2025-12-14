from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    CLERK_BACKEND_API_URL: str
    CLERK_FRONTEND_API_URL: str
    CLERK_SECRET_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


