FROM python:3.11-slim

WORKDIR /app

# Установим system-зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libmariadb-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir flask mariadb flask-socketio eventlet litestar uvicorn 

RUN chmod +x start.sh

EXPOSE 5000
EXPOSE 9100

#CMD ["sh", "-c", "echo 'Запуск пошёл'; python app.py"]

###EXAMPLES OF MULTISTART - NOT TESTED
#CMD python app.py & ; ./node_exporter
#ENTRYPOINT command && command_2 && another_command
#CMD ["python", "app.py" , "&" ; "./node_exporter"]

CMD ["./start.sh"]

STOPSIGNAL SIGINT
