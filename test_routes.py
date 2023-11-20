from fastapi import FastAPI
from fastapi.testclient import TestClient

# Import your FastAPI app here
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_get_surf_sessions():
    response = client.get("/how-is-the-surf")  # Use the client to make requests
    assert response.status_code == 200
    assert "timestamp" in response.json()
    assert "surf_data" in response.json()
