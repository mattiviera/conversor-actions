# Conversor de Unidades con FastAPI y CI

Este proyecto es un **conversor de unidades** (temperatura y distancia) desarrollado en Python con **FastAPI**, con un pipeline de **Integración Continua (CI)** configurado en **GitHub Actions**.

## Funcionalidades

- Conversión de **Celsius ↔ Fahrenheit**
- Conversión de **Kilómetros ↔ Millas**
- API REST para hacer las conversiones vía HTTP
- Pipeline de CI que:
  - Ejecuta **lint** (`flake8`)
  - Corre **tests unitarios** con cobertura (`pytest --cov`)
  - Construye el paquete (`python -m build`) y sube artefactos

## Instalación y uso

1. Clonar el repositorio:

```bash
git clone <URL_DEL_REPO>
cd conversor-actions
Crear y activar el entorno virtual:

bash
Copiar código
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Levantar la API:

bash
Copiar código
uvicorn app.main:app --reload
Probar la API en el navegador o con curl:

bash
Copiar código
# Ejemplo
curl http://127.0.0.1:8000/celsius-to-fahrenheit/25
Tests
Para correr tests y ver cobertura:

bash
Copiar código
pytest --cov=app --cov-report=term
```
