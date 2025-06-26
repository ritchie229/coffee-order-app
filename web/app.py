from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import mariadb, os, threading, time
from datetime import datetime

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

def get_db_connection():
    return mariadb.connect(
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("SHIPYARD_DOMAIN_DB", "db"),  # значение по умолчанию = db
        port=3306,
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/", methods=["GET"])
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM coffees")
    coffees = cur.fetchall()
    conn.close()
    return render_template("index.html", coffees=coffees)

@app.route("/order", methods=["POST"])
def order():
    name = request.form["name"]
    second_name = request.form["second_name"]
    coffee_id = request.form["coffee"]

    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO customers (name, second_name) VALUES (?, ?)", (name, second_name))
    customer_id = cur.lastrowid
    cur.execute("INSERT INTO orders (customer_id, coffee_id) VALUES (?, ?)", (customer_id, coffee_id))
    cur.execute("SELECT name FROM coffees WHERE id = ?", (coffee_id,))
    coffee_name = cur.fetchone()[0]
    conn.commit()
    conn.close()

    # отправим оповещение через WebSocket
    socketio.start_background_task(delayed_message, name, second_name, coffee_name)

    return f"<h2>Уважаемый {name} {second_name}, ваш кофе {coffee_name} будет готов через 1 минуту.</h2>"

def delayed_message(name, second_name, coffee_name):
    time.sleep(10)
    message = f"Заберите ваш кофе {coffee_name}, {name} {second_name}"
    socketio.emit('coffee_ready', {'message': message})

@app.route("/report")
def report():
    today = datetime.now().date()
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT c.name, c.second_name, cf.name
        FROM orders o
        JOIN customers c ON o.customer_id = c.id
        JOIN coffees cf ON o.coffee_id = cf.id
        WHERE DATE(o.order_time) = ?
    """, (today,))
    orders = cur.fetchall()
    conn.close()
    return f"<h2>Заказы на {today}:</h2>" + "<br>".join([f"{n} {s} — {coffee}" for n, s, coffee in orders])

if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5000)
