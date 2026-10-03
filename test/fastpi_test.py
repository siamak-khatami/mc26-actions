# Testing FastAPI applications using pytest and TestClient
import pytest
from fastapi.testclient import TestClient
# import httpx
from main import voting_app
from src.admin.adminSchema import AdminRegData  # Assuming your FastAPI app is defined in main.py
from utils.constants import Endpoints

# client = httpx.Client(base_url="http://localhost:8000")  # This will create a test client for the voting_app
client = TestClient(voting_app)  # This will create a test client for the voting_app
## Using testclient assumes everything is running locally. 
# However, even though th testclient is goign to use the same code as here, 
# since we have done most of the setup for the app through the docker, it will 
# miss those configs. As an exmaple, the database connection and url in the 
# app config looks over the docker assuming the api is running inside the docker.
# however here, the testclient, if we use pytest command, will not run inside the
# docker. 
# there are different methods to solve this,
# 1. Instead of using Testclient, we run docker app, and then use HTTP request for tests.
# This is simple, but will polute the dev db if we have huge ammounnt of test cases regulary.
# 2. We can make another composer for testing, with an isolated database specifically for testing
# but using the same api, and also adding a pytest service so it can have access to those things because
# pytest is running inside a container and the db name for test db service
# will autoamtically point to the test database. 
# 
def test_read_main():
    response = client.get(Endpoints.ROOT)
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the voting app!"}



# Add tests for admin registration, login, and other endpoints as needed.
# User fixtures and test cases where it is needed. 

# Testing registration endpoints for admin and users.
@pytest.mark.parametrize(
    "admin_data",
    [
        AdminRegData(email="admin1@example.com", name="admin1", password="password1"),
        AdminRegData(email="admin2@example.com", name="admin2", password="password2"),
    ]
)
def test_admin_registration(admin_data):
    payload = admin_data.model_dump(exclude={"password"})
    payload["password"] = admin_data.password.get_secret_value()
    response = client.post("/admin/register", json=payload)
    assert response.status_code == 201