import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def test_user():
    return {
        "email": "testuser@example.com",
        "password": "secure123"
    }

def test_create_user(test_user):
    response = client.post("/users/", json=test_user)
    assert response.status_code == 200
    assert "id" in response.json()
    assert response.json()["email"] == test_user["email"]

def test_get_user_by_id(test_user):
    # First, create the user
    create_response = client.post("/users/", json=test_user)
    user_id = create_response.json()["id"]

    # Now, get the user
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id