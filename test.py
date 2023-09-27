import unittest
from fastapi.testclient import TestClient
from main import app

class TestAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_hash_password_success(self):
        response = self.client.post("/hash/", json={"password": "TestPassword"})
        self.assertEqual(response.status_code, 200)
        self.assertTrue("hashed_password" in response.json())

    def test_hash_password_failure(self):
        response = self.client.post("/hash/", json={"password": "short"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Password too short"})

    def test_hash_password_unsafe(self):
        response = self.client.post("/hash/", json={"password": "unsafeee"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"detail": "Password is not secure"})


if __name__ == "__main__":
    unittest.main()