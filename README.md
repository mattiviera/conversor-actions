# Conversor de Unidades con FastAPI y CI/CD

Un **conversor de unidades** moderno y eficiente para temperatura y distancia, desarrollado con **FastAPI** e implementando un pipeline completo de **Integración Continua** con **GitHub Actions** .

## 🚀 Características

### Conversiones Disponibles

- **Temperatura** : Celsius ↔ Fahrenheit
- **Distancia** : Kilómetros ↔ Millas

### API REST

- Endpoints intuitivos para todas las conversiones
- Respuestas en formato JSON
- Validación automática de parámetros
- Documentación interactiva automática

### Endpoint de Salud

- **`/health`** : Monitoreo del estado del servicio
- Retorna `{"status": "ok", "timestamp": "2025-01-01T12:00:00Z"}`
- Incluye `"api_key_configurada": true` si la variable de entorno `MY_API_KEY` está configurada.
- Permite que pipelines y herramientas de monitoreo verifiquen si el servicio está levantado y la API key está disponible.
- Timestamp en formato ISO UTC
- Ideal para pipelines y herramientas de monitoreo

### Pipeline CI/CD

- ✅ **Linting** : Análisis de código con `flake8`
- ✅ **Testing** : Tests unitarios con `pytest`
- ✅ **Cobertura** : Reportes de cobertura de código (>90%)
- ✅ **Build** : Construcción automática del paquete
- ✅ **Artefactos** : Subida automática de builds

## 📋 Requisitos Previos

- Python 3.8+
- pip
- Git

## 🛠️ Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/mattiviera/conversor-actions.git
cd conversor-actions
```

### 2. Crear entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# En Windows:
venv\Scripts\activate

# En macOS/Linux:
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

## 🚦 Uso

### Levantar el servidor

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en: `http://127.0.0.1:8000`

### Ejemplos de uso

#### Conversión de temperatura

```bash
# Celsius a Fahrenheit
curl http://127.0.0.1:8000/celsius-to-fahrenheit/25
# Respuesta: {"celsius": 25, "fahrenheit": 77.0}

# Fahrenheit a Celsius
curl http://127.0.0.1:8000/fahrenheit-to-celsius/77
# Respuesta: {"fahrenheit": 77, "celsius": 25.0}
```

#### Conversión de distancia

```bash
# Kilómetros a Millas
curl http://127.0.0.1:8000/km-to-miles/10
# Respuesta: {"kilometers": 10, "miles": 6.214}

# Millas a Kilómetros
curl http://127.0.0.1:8000/miles-to-km/6.214
# Respuesta: {"miles": 6.214, "kilometers": 10.0}
```

#### Verificar salud del servicio

```bash
curl http://127.0.0.1:8000/health
# Respuesta: {"status": "ok", "timestamp": "2025-09-25T10:30:45.123Z"}
```

## 🧪 Testing

### Ejecutar tests

```bash
# Tests básicos
pytest

# Tests con cobertura
pytest --cov=app --cov-report=term

# Tests con reporte HTML
pytest --cov=app --cov-report=html
```

### Cobertura de Tests

- **Objetivo** : Cobertura mínima del 90%
- **Actual** : 100% de cobertura
- **Incluye** : Tests unitarios para todos los endpoints y funciones de conversión

#### Tests del endpoint `/health`

- ✅ Verifica status code 200
- ✅ Valida estructura JSON de respuesta
- ✅ Confirma formato ISO del timestamp
- ✅ Comprueba valor correcto del status

## 📚 Documentación

### Documentación Interactiva

Una vez levantado el servidor, accede a la documentación automática:

- **Swagger UI** : `http://127.0.0.1:8000/docs`
- **ReDoc** : `http://127.0.0.1:8000/redoc`

### Endpoints Disponibles

| Método | Endpoint                         | Descripción                    |
| ------ | -------------------------------- | ------------------------------ |
| GET    | `/health`                        | Estado del servicio            |
| GET    | `/celsius-to-fahrenheit/{value}` | Convierte Celsius a Fahrenheit |
| GET    | `/fahrenheit-to-celsius/{value}` | Convierte Fahrenheit a Celsius |
| GET    | `/km-to-miles/{value}`           | Convierte Kilómetros a Millas  |
| GET    | `/miles-to-km/{value}`           | Convierte Millas a Kilómetros  |

## 🔄 CI/CD Pipeline

### Workflow de GitHub Actions

El pipeline se ejecuta automáticamente en cada push y pull request:

1. **Setup** : Configuración del entorno Python
2. **Dependencies** : Instalación de dependencias
3. **Lint** : Análisis de código con flake8
4. **Test** : Ejecución de tests unitarios
5. **Coverage** : Verificación de cobertura mínima
6. **Build** : Construcción del paquete distribuible
7. **Artifacts** : Subida de artefactos del build

### Badges de Estado

```markdown
![CI](https://github.com/usuario/conversor-actions/workflows/CI/badge.svg)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![Python](https://img.shields.io/badge/python-3.8+-blue)
```

## 🏗️ Estructura del Proyecto

```
conversor-actions/
├── app/
│   ├── __init__.py
│   ├── main.py          # Aplicación FastAPI principal
│   └── conversor.py    # Lógica de conversiones
├── tests/
│   ├── __init__.py
│   ├── test_api.py     # Tests de endpoints
│   ├── test_conversor.py # Tests de conversiones
│   └── test_health.py # Tests de status
├── .github/
│   └── workflows/
│       └── ci.yml       # Configuración CI/CD
├── requirements.txt     # Dependencias del proyecto
├── pyproject.toml            # Configuración del paquete
└── README.md           # Este archivo
```

### Estándares de Código

- Seguir PEP 8
- Cobertura de tests mínima: 90%
- Todos los tests deben pasar
- Lint sin errores
