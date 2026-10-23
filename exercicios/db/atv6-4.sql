USE ecommerce;

SET SQL_SAFE_UPDATES = 0;

SELECT * FROM produtos;

UPDATE produtos SET preco = preco + preco * 0.08
WHERE estoque < 20;

UPDATE produtos SET preco = 0
WHERE preco < 0;

UPDATE produtos SET preco = preco + preco * 0.12
WHERE nome LIKE '%Logitech%';

UPDATE produtos SET estoque = estoque -1
WHERE nome = 'PS5 Pro';

UPDATE produtos SET preco = preco - preco * 0.05
WHERE nome LIKE '%Memoria%';

UPDATE produtos SET categoria_id = 1
WHERE categoria_id = null;

UPDATE produtos SET estoque = 100;