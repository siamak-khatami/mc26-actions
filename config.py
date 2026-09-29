from pydantic_settings import BaseSettings
from sqlalchemy.engine.url import URL
from pydantic import SecretStr


class Settings(BaseSettings):
    ADMIN_JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    ADMIN_JWT_EXPIRE_DAYS: int = 1
    POSTGRES_USER: str
    POSTGRES_PASSWORD: SecretStr
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    def get_postgres_url(self, HOST: str = None, PORT: int = 5432) -> str:
        # The format for the PostgreSQL URL is:
        # postgresql://<user>:<password>@<host>/<database>
        return URL.create(
            drivername="postgresql+psycopg2",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD.get_secret_value(),
            host=HOST if HOST is not None else self.POSTGRES_HOST,
            port=PORT if PORT is not None else self.POSTGRES_PORT,
            database=self.POSTGRES_DB
        )


    class Config:
        env_file = ".env"
