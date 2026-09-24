# This is the main entry point for the API using fastapi

from fastapi import FastAPI
from utils.constants import Endpoints
import uvicorn
from src.admin.adminEndpoints import admin_router

voting_app = FastAPI(
    title="Voting App",
    description="API for the voting application",
    version="1.0.0",
    contact={
        "name": "API Support",
        "url": "http://www.example.com/support",
        "email": "support@example.com",
    },
    docs_url="/docs",
    redoc_url="/redoc",
)


# Attaching routers
voting_app.include_router(admin_router)


@voting_app.get(Endpoints.ROOT)
def read_root():
    return {"message": "Welcome to the voting app!"}


if __name__ == "__main__":
    uvicorn.run("main:voting_app", host="0.0.0.0", port=8000, reload=True)