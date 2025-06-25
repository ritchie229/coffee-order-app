from flask import Flask, render_template, request, redirect, url_for
import mariadb
import os
import threading
import time
from datetime import datetime

app = Flask(__name__)

def get_db_connection():
    return mariadb.connect(
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host="db",
        port=3306,
        database=os.getenv("MYSQL_DATABASE")
    )

@app.route("/", methods=["GET", "POST"])
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

    threading.Thread(target=delayed_message, args=(name, second_name, coffee_name)).start()
    return f"<h2>Уважаемый {name} {second_name}, ваш кофе {coffee_name} будет готов через 1 минуту.</h2>"

def delayed_message(name, second_name, coffee_name):
    time.sleep(60)
    print(f"Заберите ваш кофе {coffee_name}, {name} {second_name}")

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
    app.run(host="0.0.0.0", port=5000)
