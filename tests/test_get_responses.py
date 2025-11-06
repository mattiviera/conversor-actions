from fastapi.testclient import TestClient
from app.main import app, redis_client

client = TestClient(app)

def test_get_responses():
    # Crear token temporal en Redis
    token = "test-token"
    redis_client.set(f"token:{token}", "true")


    # Hacer request con el token en el header
    response = client.get(
        "/get-responses",
        headers={"Authorization": f"Bearer {token}"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "total" in data
    assert "records" in data

    # Limpiar token después del test
    redis_client.delete(f"token:{token}")
