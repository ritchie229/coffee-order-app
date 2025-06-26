FROM python:3.11-slim

WORKDIR /app

# Установим system-зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir flask mariadb flask-socketio eventlet

CMD ["sh", "-c", "echo 'Запуск пошёл'; python app.py"]
#CMD ["python", "app.py"]
