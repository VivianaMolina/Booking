FROM python:3.10

WORKDIR /flask_app

# Copiar solo requirements primero (mejor cache)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Ahora sí copiar el resto del proyecto
COPY . .

EXPOSE 5000

CMD ["python", "server.py"]