-- Создаём пользователя с mysql_native_password
ALTER USER 'coffee_user'@'%' IDENTIFIED WITH mysql_native_password BY 'coffee_pass';

-- На всякий случай создаём пользователя, если его нет
CREATE USER IF NOT EXISTS 'coffee_user'@'%' IDENTIFIED WITH mysql_native_password BY 'coffee_pass';

-- Даём права
GRANT ALL PRIVILEGES ON coffee_shop.* TO 'coffee_user'@'%';
FLUSH PRIVILEGES;


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
