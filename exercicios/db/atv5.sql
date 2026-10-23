USE ecommerce;

SELECT * FROM produtos;

SELECT nome, preco FROM produtos;

SELECT nome, preco FROM produtos
WHERE preco > 500;

SELECT nome, preco, estoque FROM produtos
WHERE estoque < 20
ORDER BY preco ASC;

SELECT nome, preco FROM produtos
WHERE nome LIKE '%PS5%';

SELECT nome, preco FROM produtos
ORDER BY preco DESC
LIMIT 2;

SELECT COUNT(*) AS qtd_produtos FROM produtos;

SELECT SUM(estoque) AS total_estoque FROM produtos;

SELECT ROUND(AVG(preco), 2) AS preco_medio FROM produtos;

SELECT MIN(preco) AS menor, MAX(preco) AS maior
FROM produtos;