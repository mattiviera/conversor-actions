from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    data = response.json()
    # Verificar campos obligatorios
    assert "status" in data
    assert data["status"] == "ok"           # Coincide con el endpoint corregido
    assert "timestamp" in data
    assert "client_ip" in data               # Cambiado de "client" a "client_ip" para que coincida con main.py
