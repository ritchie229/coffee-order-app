CREATE TABLE IF NOT EXISTS customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    second_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS coffees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50)
);

INSERT INTO coffees (name) VALUES
('Latte'), ('Capuchino'), ('Mocachino'), ('Espresso'), ('Americano');

CREATE TABLE IF NOT EXISTS orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    coffee_id INT,
    order_time DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (coffee_id) REFERENCES coffees(id)
);
