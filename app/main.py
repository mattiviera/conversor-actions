import os
from fastapi import FastAPI, Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.conversor import (
    celsius_a_fahrenheit,
    fahrenheit_a_celsius,
    km_a_millas,
    millas_a_km,
)
from datetime import datetime, timezone
from dotenv import load_dotenv
import redis
from sqlalchemy import insert, select, delete
from app.database import engine, health_logs

load_dotenv()

app = FastAPI()
API_KEY = os.environ.get("MY_API_KEY")

# Configuración Redis
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

# ------------------- Security / Bearer Token -------------------
bearer_scheme = HTTPBearer()


async def validate_token_dependency(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
):
    """Valida el token JWT usando Redis."""
    token = credentials.credentials
    if not redis_client.exists(f"token:{token}"):
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return token


# ------------------- Endpoints principales -------------------
@app.get("/")
def root():
    return {"message": "Bienvenido al conversor de unidades"}


@app.get("/celsius-to-fahrenheit/{c}")
def api_celsius_to_fahrenheit(c: float):
    return {"fahrenheit": celsius_a_fahrenheit(c)}


@app.get("/fahrenheit-to-celsius/{f}")
def api_fahrenheit_to_celsius(f: float):
    return {"celsius": fahrenheit_a_celsius(f)}


@app.get("/km-to-miles/{km}")
def api_km_to_miles(km: float):
    return {"miles": km_a_millas(km)}


@app.get("/miles-to-km/{miles}")
def api_miles_to_km(miles: float):
    return {"km": millas_a_km(miles)}


@app.get("/health", tags=["Health"])
async def health_check():
    """Endpoint para verificar si el servicio está levantado."""
    return {
        "status": "ok",
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "api_key_configurada": API_KEY is not None,
    }


@app.get("/ping", tags=["Health"])
async def ping(request: Request):
    """Guarda información de ping en Redis y en la base de datos."""
    timestamp = datetime.now(timezone.utc)
    client_ip = request.client.host
    api_key = API_KEY if API_KEY else "no-key"

    # Guardar en Redis
    redis_key = f"ping:{timestamp.isoformat()}"
    redis_client.hset(
        redis_key,
        mapping={
            "timestamp": timestamp.isoformat(),
            "client_ip": client_ip,
            "api_key": api_key,
        },
    )

    # Guardar en base de datos
    stmt = insert(health_logs).values(
        timestamp=timestamp, client_ip=client_ip, api_key=api_key
    )
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return {"status": "ok", "timestamp": timestamp.isoformat(), "client_ip": client_ip}


@app.get("/get-responses", tags=["Health"])
async def get_responses(token: str = Depends(validate_token_dependency)):
    """Devuelve todos los registros guardados en la base de datos (requiere token)."""
    stmt = select(health_logs)
    with engine.connect() as conn:
        results = conn.execute(stmt).fetchall()

    data = [
        {
            "timestamp": row.timestamp.isoformat()
            if isinstance(row.timestamp, datetime)
            else str(row.timestamp),
            "client_ip": row.client_ip,
            "api_key": row.api_key,
        }
        for row in results
    ]

    return {"total": len(data), "records": data}


@app.delete("/clear-responses", tags=["Health"])
async def clear_responses():
    """Elimina todas las respuestas guardadas en Redis y base de datos."""
    # Limpiar Redis
    for key in redis_client.scan_iter("ping:*"):
        redis_client.delete(key)

    # Limpiar base de datos
    stmt = delete(health_logs)
    with engine.connect() as conn:
        conn.execute(stmt)
        conn.commit()

    return {"message": "All responses have been cleared successfully"}
