CREATE DATABASE IF NOT EXISTS estoque;

USE estoque;

CREATE TABLE categorias (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE produtos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    quantidade INT NOT NULL,
    categoria_id INT NOT NULL,

    FOREIGN KEY (categoria_id)
        REFERENCES categorias(id)
);