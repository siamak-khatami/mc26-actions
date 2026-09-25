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


class AdminLoginResponse(BaseModel):
    message: str = "Admin logged in successfully."
    token: str


class AdminValidateResponse(BaseModel):
    message: str = "Admin token is valid."
    admin_payload: dict