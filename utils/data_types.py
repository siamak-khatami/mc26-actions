from pydantic import BaseModel
from datetime import datetime, timedelta
from config import Settings
settings = Settings()


class AdminJWTPayload(BaseModel):
    email: str
    exp: datetime = datetime.now() + timedelta(days=settings.ADMIN_JWT_EXPIRE_DAYS)