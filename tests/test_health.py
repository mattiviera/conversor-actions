import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Para Windows si pytest no encuentra main

from fastapi.testclient import TestClient
from app.main import app
from datetime import datetime

client = TestClient(app)

def test_health_endpoint_status():
    response = client.get("/health")
    assert response.status_code == 200, "El endpoint /health debe devolver status 200"

def test_health_endpoint_json():
    response = client.get("/health")
    json_data = response.json()
    assert "status" in json_data and json_data["status"] == "ok", "El JSON debe contener status ok"
    assert "timestamp" in json_data, "El JSON debe contener un timestamp"
    
    # Validar formato ISO del timestamp
    try:
        datetime.fromisoformat(json_data["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        assert False, "El timestamp no está en formato ISO válido"
