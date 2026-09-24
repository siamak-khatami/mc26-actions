from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    ADMIN_JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ADMIN_JWT_EXPIRE_DAYS: int = 1

    class Config:
        env_file = ".env"
