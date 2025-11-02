FROM python:3.12-slim

WORKDIR /app

# Instalar dependências
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar código
COPY . .

# Expor porta para a API
EXPOSE 8000

# Comando para iniciar a API FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]