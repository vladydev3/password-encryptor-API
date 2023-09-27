from fastapi.testclient import TestClient
from main import app
from main import verify

client = TestClient(app)

def test_hash_password():
    response = client.post("/hash/", json={"password": "test1234"})
    assert response.status_code == 200
    assert "hashed_password" in response.json()
    assert "security" in response.json()

def test_hash_password_short_password():
    response = client.post("/hash/", json={"password": "test"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password too short"}

def test_hash_password_unsafe_password():
    response = client.post("/hash/", json={"password": "password"})
    assert response.status_code == 400
    assert response.json() == {"detail": "Password is not secure"}

def test_verify_unsafe_password():
    assert verify("password") == "unsafe"

def test_verify_moderately_safe_password():
    assert verify("Password123") == "moderately safe"

def test_verify_secure_password():
    assert verify("SecurePassword123") == "secure password"