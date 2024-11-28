-- Cria o banco de dados
DROP DATABASE IF EXISTS produtos_ti;
CREATE DATABASE produtos_ti;

-- Usa o banco criado
USE produtos_ti;

-- Cria a tabela produto
CREATE TABLE IF NOT EXISTS produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    descricao TEXT,
    preco DECIMAL(10, 2) NOT NULL
);

-- Insere 10 produtos relacionados à área de TI
INSERT INTO produto (nome, descricao, preco) VALUES
('Teclado Mecânico', 'Teclado mecânico RGB com switches Cherry MX Red.', 250.00),
('Mouse Gamer', 'Mouse óptico com DPI ajustável e iluminação RGB.', 150.00),
('Monitor 24"', 'Monitor LED Full HD com taxa de atualização de 144Hz.', 900.00),
('Fone de Ouvido', 'Fone com som estéreo e cancelamento de ruído.', 300.00),
('Notebook', 'Notebook com processador Intel i7 e 16GB de RAM.', 4500.00),
('SSD 1TB', 'Unidade de armazenamento SSD com leitura ultrarrápida.', 800.00),
('Placa de Vídeo', 'Placa gráfica NVIDIA RTX 3060 com 12GB GDDR6.', 2500.00),
('Gabinete', 'Gabinete ATX com painel de vidro temperado.', 350.00),
('Fonte 600W', 'Fonte de alimentação com certificação 80 Plus Bronze.', 450.00),
('Cadeira Gamer', 'Cadeira ergonômica com ajuste de altura e encosto reclinável.', 1200.00);

SELECT * FROM produto;