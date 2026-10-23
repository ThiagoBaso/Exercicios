CREATE DATABASE ecomerce CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci

USE ecomerce;

CREATE TABLE clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);

SELECT * FROM clientes;

INSERT INTO clientes (nome, email, telefone)
VALUES 
('Maria SIlva', 'ms@gmail.com', '14999999999'),
('Thiago Baso', 'baso@gmacil.com', '14888888888'),
('Pedro Marcelo', 'pm@gamail.com', '1477777777');

