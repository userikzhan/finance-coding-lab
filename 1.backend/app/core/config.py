from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):

    # PostgreSQL
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Refresh token
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()
