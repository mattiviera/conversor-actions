# Usamos Python oficial
FROM python:3.12-slim

# Seteamos el directorio de trabajo
WORKDIR /app

# Copiamos requirements
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiamos la app
COPY app ./app

# Exponemos el puerto
EXPOSE 8000

# Comando para levantar FastAPI con uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
