CREATE DATABASE IF NOT EXISTS estoque;

USE estoque;

CREATE TABLE categoria (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    categoria INT NOT NULL,

    FOREIGN KEY (categoria)
        REFERENCES categoria(id)
);

DELIMITER $$
CREATE PROCEDURE cadastrar_categoria(IN c_nome VARCHAR(100))
BEGIN
    INSERT INTO categoria (nome)
    VALUES (c_nome);
END $$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE cadastrar_produto(
    IN p_nome VARCHAR(100),
    IN p_preco DECIMAL(10,2),
    IN p_quantidade INT,
    IN p_categoria_id INT
)
BEGIN
    INSERT INTO produto (nome, preco, quantidade, categoria)
    VALUES (p_nome, p_preco, p_quantidade, p_categoria_id);
END $$
DELIMITER ;