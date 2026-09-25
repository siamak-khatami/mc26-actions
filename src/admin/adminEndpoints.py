# We will make fastaip router here for admins

from fastapi import APIRouter, status, Depends, HTTPException
from utils.security import validate_jwt_token
from utils.security import hash_password, verify_and_update_password, generate_jwt
from utils.constants import Endpoints
from src.admin.adminSchema import AdminRegData, AdminLoginData, AdminRegResponse, AdminLoginResponse, AdminValidateResponse
from utils.data_types import AdminJWTPayload
from utils.db import get_db

# Importing logger for logging purposes
from logger import get_logger
logger = get_logger()


admin_router = APIRouter(prefix=Endpoints.ADMIN, tags=["admin"])

#Checklist to have a good practice in endpoint desing,
# 1. Read strgins like endpoints from a constant file
# 2. Include status code
# 3. Define request and response models for clarity and validation
# 4. Use Depends for dependency injection, like database sessions or authentication.
#    This will ensure endpoint pre-requesits like authenticatio has been done before the actual endpoint logic is executed.
# 5. Pay attention to ignore files.
# 6. Add packages with a package manager.


# Registration endpoint
@admin_router.post(Endpoints.REGISTER, 
                   status_code=status.HTTP_201_CREATED,
                   response_model=AdminRegResponse)
def register_admin(admin_reg_data: AdminRegData, db=Depends(get_db)):
    # First we need to have db somewhere to save this info
    # We NEVER save senstive information in a db as their inital form.
    # Based on the future expected usecases, we may have 2 scenarios.
    # 1. Saving credentials: We need to save them in an encrypted form which is not possible to 
    # decrypt them back, but meanwhile to verify them.
    # 2. Savinf other information that requires decryption later, like messages:
    # then we need to use a reversible encryption method, usually with addition secrets saved alongside.
    # Hashing the password before saving
    admin_reg_data.password = hash_password(admin_reg_data.password)
    try:
        db.add_admin(admin_reg_data)
    except Exception as e:
        logger.error(f"Error registering admin: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error.")
    # db.add_admin(admin_reg_data)  # This line is now redundant and should be removed
    logger.info(f"Admin registered: {admin_reg_data.email}")
    return AdminRegResponse(
        name=admin_reg_data.name,
        email=admin_reg_data.email
    )
 
@admin_router.post(Endpoints.LOGIN,
                   status_code=status.HTTP_200_OK,
                   response_model=AdminLoginResponse)
def login_admin(admin_login_data: AdminLoginData, db=Depends(get_db)):
    # First we verify the email and that the user exists in the database.
    admin = db.get_admin(admin_login_data.email)
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Admin not found.")
    # now time to verify the password
    if not verify_and_update_password(admin_login_data.password, admin.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid password.")

    # Generating JWT to return to the user
    payload = AdminJWTPayload(email=admin.email)
    jwt_token = generate_jwt(payload) 
    return AdminLoginResponse(
        token=jwt_token
    )

@admin_router.post(Endpoints.VALIDATE)
def validate_admin(admin_payload=Depends(validate_jwt_token),
                   status_code=status.HTTP_200_OK,
                   response_model=AdminValidateResponse)
def validate_admin(admin_payload=Depends(validate_jwt_token)):
    return AdminValidateResponse(
        admin_payload=admin_payload.model_dump()
    )

@admin_router.get(Endpoints.ROOT)
def read_admin():
    return {"message": "Welcome to the admin panel!"}