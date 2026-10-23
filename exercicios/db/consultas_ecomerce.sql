USE ecomerce;

SELECT nome AS apelido, email FROM clientes;

SELECT id, nome AS apelido FROM clientes
WHERE nome LIKE '%baso%' OR id = 3;

DROP DATABASE ecomerce;

-- entre = BETWEEN
SELECT * FROM produtos
WHERE estoque BETWEEN 10 AND 20;

SELECT * FROM produtos
WHERE nome IN ('Mouse Logitech', 'Teclado Redragon');

SELECT * FROM produtos
WHERE nome NOT LIKE '%teclado%'
ORDER BY preco DESC;

SELECT * FROM produtos
ORDER BY preco ASC
LIMIT 3;

SELECT nome, preco, estoque, preco * estoque AS total
FROM produtos
ORDER BY total ASC;

SELECT COUNT(*) AS qtd_produtos FROM produtos;

SELECT SUM(preco * estoque) AS total FROM produtos;

SELECT AVG(estoque) FROM produtos; -- media

SELECT MAX(preco) AS mais_caro, MIN(preco) AS mais_barato
FROM produtos;

SELECT ROUND(AVG(preco), 2) FROM produtos;

SELECT COUNT(*) FROM produtos
WHERE preco > 250;


