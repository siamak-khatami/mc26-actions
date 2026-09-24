# Here we are holding the security funcions to be used by other parts of the application.

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from passlib.context import CryptContext
from passlib.context import CryptContext
from pydantic import SecretStr
from jose import jwt
from pygments import token
from config import Settings
from utils.data_types import AdminJWTPayload
settings = Settings()

def hash_context() -> CryptContext:
    return CryptContext(schemes=["bcrypt", "sha256_crypt", "argon2"], deprecated="auto")


def hash_password(password: SecretStr) -> str:
    context = hash_context()
    return context.hash(password.get_secret_value())

def verify_password(password: SecretStr, hashed_password: str) -> bool:
    context = hash_context()
    return context.verify(password.get_secret_value(), hashed_password)


def verify_and_update_password(password: SecretStr, hashed_password: str) -> tuple[bool, str]:
    context = hash_context()
    verified, new_hash = context.verify_and_update(password.get_secret_value(), hashed_password)
    if new_hash is not None:
        hashed_password = new_hash
    return verified, hashed_password


def generate_jwt(payload: AdminJWTPayload) -> str:
    return jwt.encode(payload.model_dump(), 
                      settings.ADMIN_JWT_SECRET, 
                      algorithm=settings.JWT_ALGORITHM)


oauth2_schema = HTTPBearer() 
def validate_jwt_token(header: HTTPAuthorizationCredentials = Depends(oauth2_schema)) -> dict:
    try: 
        payload_data = jwt.decode(header.credentials, settings.ADMIN_JWT_SECRET, algorithms=settings.JWT_ALGORITHM)
        return payload_data
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid JWT token.")