from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Bienvenido al conversor de unidades"}


def test_celsius_to_fahrenheit():
    response = client.get("/celsius-to-fahrenheit/0")
    assert response.json() == {"fahrenheit": 32.0}


def test_fahrenheit_to_celsius():
    response = client.get("/fahrenheit-to-celsius/32")
    assert response.json() == {"celsius": 0.0}


def test_km_to_miles():
    response = client.get("/km-to-miles/10")
    assert round(response.json()["miles"], 5) == 6.21371


def test_miles_to_km():
    response = client.get("/miles-to-km/6.21371")
    assert round(response.json()["km"], 5) == 10
