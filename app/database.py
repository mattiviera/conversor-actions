from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
from sqlalchemy.sql import func
import os

# Para desarrollo local, usamos SQLite
DATABASE_URL = os.environ.get("DATABASE_URL", "sqlite:///./health.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()

# Tabla para guardar logs de health/ping
health_logs = Table(
    "health_logs",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("timestamp", DateTime, default=func.now()),
    Column("client_ip", String),
    Column("api_key", String),
)

# Crear tabla si no existe
metadata.create_all(engine)
