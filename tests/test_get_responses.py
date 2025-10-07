from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_responses():
    response = client.get("/get-responses")
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "records" in data
