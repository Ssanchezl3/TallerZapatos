# 🔹 Imagen base ligera de Python
FROM python:3.11-slim

# 🔹 Configurar directorio de trabajo
WORKDIR /app

# 🔹 Copiar dependencias
COPY requirements.txt .

# 🔹 Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 🔹 Co
