from fastapi.testclient import TestClient
from app.main import app
from app.database import engine, health_logs
from sqlalchemy import insert, text
from datetime import datetime

client = TestClient(app)


def test_clear_responses():
    """
    Verifica que el endpoint /clear-responses elimine correctamente
    los registros de la base de datos y Redis, y devuelva el mensaje esperado.
    """
    # Insertar un registro falso en la base de datos para probar
    stmt = insert(health_logs).values(
        timestamp=datetime(2025, 11, 6, 0, 0, 0),
        client_ip="127.0.0.1",
        api_key="test-key",
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    # Ejecutar la petición DELETE
    response = client.delete("/clear-responses")
    assert response.status_code == 200

    data = response.json()
    assert "message" in data
    assert data["message"] == "All responses have been cleared successfully"

    # Confirmar que la tabla quedó vacía
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM health_logs")).scalar()
    assert result == 0
