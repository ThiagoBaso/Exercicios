CREATE DATABASE ecommerce CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci;

USE ecommerce;

-- Entidade/tabela clientes

CREATE TABLE clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);
-- Visualizar registros da nossa tabela
SELECT * FROM clientes;
-- INSERINDO REGISTROS
INSERT INTO clientes (nome, email, telefone)
VALUES
('Maria Silva', 'maria@gmail.com', '14979875487'),
('João Vitor', 'joao@email.com', '14478156825');

CREATE TABLE teste (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    telefone VARCHAR(20)
);
-- Apagar tabela
DROP TABLE teste;

CREATE TABLE categorias (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome VARCHAR(100) NOT NULL
);

CREATE TABLE produtos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL (10, 2) NOT NULL,
    estoque INT DEFAULT 0,
    categoria_id INT,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

SELECT * FROM produtos;

INSERT INTO categorias (nome)
VALUES
('Periféricos'),
('Audio'),
('Informática');

SELECT * FROM categorias;

INSERT INTO produtos (nome, preco, estoque, categoria_id)
VALUES 
('Mouse Logitech', 400.00, 20, 1),
('Caixa de som JBL', 200.00, 2, 2),
('Monitor AlienWare', 3000.00, 15, 3),
('Teclado Redragon', 250.00, 10, 1),
('Headset HyperX', 350.00, 5, 2);

SELECT * FROM produtos;

CREATE TABLE pedidos (
	id 	INT AUTO_INCREMENT PRIMARY KEY,
    cliente_id INT NOT NULL,
    data_pedido DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

CREATE TABLE pedidos_has_produtos (
	id INT AUTO_INCREMENT PRIMARY KEY,
    pedido_id INT NOT NULL,
    produto_id INT NOT NULL,
    quantidade INT DEFAULT 1,
    preco_unitario DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedidos(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO pedidos (cliente_id)
VALUES 
(1),
(2);

SELECT * FROM produtos;

INSERT INTO pedidos_has_produtos (pedido_id, produto_id, quantidade, preco_unitario)
VALUES 
(1, 2, 1, 180.00), -- pedido 1 da Maria
(1, 4, 2, 250.00), -- pedido 1 da Maria (Maria comprou 2 produtos diferentes em um mesmo pedido) 
(2, 5, 1, 300.00); -- pedido 2 do Joao