from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    # PostgreSQL
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str

    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Refresh token
    REFRESH_TOKEN_EXPIRE_DAYS: int = 30

    class Config:
        env_file = ".env"


settings = Settings()
