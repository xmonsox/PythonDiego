CREATE DATABASE personal_finances CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

USE personal_finances;

CREATE TABLE users (
    user_id CHAR(30) PRIMARY KEY,
    full_name VARCHAR(80),
    mail VARCHAR(100) UNIQUE, -- user_name
    passhash VARCHAR(140),
    user_role ENUM('admin','user'),
    balance FLOAT(10,2),
    user_status TINYINT(1) DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);


INSERT INTO users (user_id, full_name, mail, passhash, user_role, balance, user_status) VALUES ('1A', 'Monsalve', 'monso@gmail.com', '12345', 'user', '10000', 1 );


CREATE TABLE category (
    category_id SMALLINT(3) AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50),
    category_description VARCHAR(120),
    category_status TINYINT(1) DEFAULT 1
);
INSERT INTO category (category_name, category_description)
VALUES ('Electronica', 'Productos electronicos'),
       ('Ropa', 'Ropa para hombres y mujeres'),
       ('Hogar', 'Articulos para el hogar'),
       ('Deportes', 'Equipamiento deportivo para diversas disciplinas');


CREATE TABLE transactions (
    transactions_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    user_id CHAR(30),
    category_id SMALLINT(3),
    amount FLOAT(10,2), --Monto
    t_description VARCHAR(120),
    t_type ENUM('revenue','expenses'),
    t_date DATE,
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (category_id) REFERENCES category (category_id)
);

CREATE TABLE history_transactions (
    history_id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    transactions_id INT UNSIGNED,
    user_id CHAR(30),
    category_id SMALLINT(3),
    amount FLOAT(10,2), --monto
    t_description VARCHAR(120),
    t_type ENUM('revenue','expenses'), -- ingresos -- gastos
    t_date DATE, 
    FOREIGN KEY (user_id) REFERENCES users (user_id),
    FOREIGN KEY (category_id) REFERENCES category (category_id)
);



-- PROCEDIMIENTOS ALMACENADOS.

-- Crear un procedimiento almacenado para insertar una transacción. Pero si la transacción es un gasto, verificar primero si tiene saldo para hacer ese gasto.

DELIMITER //
CREATE PROCEDURE insertTransaccion(IN id CHAR(10), IN categoria_id INT, IN monto FLOAT(10,2), IN descr VARCHAR(255), IN tipo VARCHAR(50), IN fecha DATE )
BEGIN 
    DECLARE tipo_trans VARCHAR(50);
    DECLARE monto_p FLOAT(10,2);
    DECLARE balan FLOAT(10,2);

    SET tipo_trans = tipo;
    SET monto_p = monto;
    SET balan = (SELECT balance FROM users WHERE user_id = id);

    IF tipo_trans = "expenses" THEN
        IF balan >= monto_p THEN
            INSERT INTO transactions (user_id, category_id, amount, t_description, t_type, t_date) VALUES (id, categoria_id, monto, descr, tipo, fecha);
            UPDATE users SET balance = balance - monto WHERE user_id = id;
        ELSE 
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'NO HAY SUFICIENTE SALDO';
        END IF;
    ELSEIF tipo_trans = "revenue" THEN 
        INSERT INTO transactions (user_id, category_id, amount, t_description, t_type, t_date) VALUES (id, categoria_id, monto, descr, tipo, fecha);
        UPDATE users SET balance = balance + monto WHERE user_id = id;
    END IF;
END //
DELIMITER ;

-- Crear un procedimiento almacenado para que cuando un usuario actualice una transacción guarde los datos antiguos en la tabla historico de transacciones. 
DELIMITER //
CREATE PROCEDURE updatetrans(IN id_trans INT ,IN new_id CHAR(10), IN new_categoria_id INT, IN new_monto FLOAT(10,2), IN new_descr VARCHAR(255), IN new_tipo VARCHAR(50), IN new_fecha DATE )
BEGIN
    DECLARE old_user_id CHAR(10);
    DECLARE old_categoria_id INT;
    DECLARE old_monto FLOAT(10,2);
    DECLARE old_description VARCHAR(255);
    DECLARE old_tipo VARCHAR(50);
    DECLARE old_fecha DATE;

    DECLARE id_transaccion INT;
    DECLARE n_monto FLOAT(10,2);
    DECLARE balan FLOAT(10,2);
    DECLARE tipo_recibe VARCHAR(50);
    SET tipo_recibe = new_tipo;

    SET balan = (SELECT balance FROM users WHERE user_id = new_id);
    SET n_monto = new_monto;
    SET id_transaccion = id_trans;

    SELECT user_id, category_id, amount, t_description, t_type, t_date
    INTO old_user_id, old_categoria_id, old_monto, old_description, old_tipo, old_fecha
    FROM transactions
    WHERE transactions_id  = id_transaccion AND user_id = new_id;

    INSERT INTO history_transactions (transactions_id, user_id, category_id, amount, t_description, t_type, t_date) VALUES (old_user_id, old_categoria_id, old_monto, old_description, old_tipo, old_fecha);

    UPDATE users SET balance = balance + old_monto WHERE user_id = id;

    IF tipo_recibe = "expenses" THEN
        IF balan >= n_monto THEN
            UPDATE transactions 
            SET transactions_id = id_transaccion, user_id = new_id, category_id = new_categoria_id, amount = new_monto, t_description = new_descr, t_type = new_tipo, t_date = new_fecha 
            WHERE transactions_id = id_transaccion;
            UPDATE users SET balance = balance - new_monto WHERE user_id = new_id;
        ELSE 
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'NO HAY SUFICIENTE SALDO';
        END IF;
    ELSEIF tipo_recibe = "revenue" THEN 
            UPDATE transactions 
            SET transactions_id = id_transaccion, user_id = new_id, category_id = new_categoria_id, amount = new_monto, t_description = new_descr, t_type = new_tipo, t_date = new_fecha 
            WHERE transactions_id = id_transaccion;
            UPDATE users SET balance = balance + new_monto WHERE user_id = new_id;
    END IF;
    
    
END //
DELIMITER;  

DELIMITER //
CREATE FUNCTION total_dia (fecha_dia DATE) RETURNS FLOAT(10,2)
BEGIN
    DECLARE tota|l FLOAT(10,2);
    SELECT SUM(amount) INTO total FROM transactions WHERE t_type = "expenses"  AND t_date = fecha_dia;
    RETURN total;
END
//
DELIMITER;
