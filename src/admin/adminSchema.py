from pydantic import BaseModel, EmailStr, SecretStr


class AdminRegData(BaseModel):
    name: str
    email: EmailStr
    password: SecretStr


class AdminRegResponse(BaseModel):
    message: str = "Admin registered successfully."
    name: str
    email: EmailStr


class AdminLoginData(BaseModel):
    email: EmailStr
    password: SecretStr