-- Criação da tabela de produtos
CREATE TABLE produtos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    marca VARCHAR(100) NOT NULL,
    preco DECIMAL(10,2) NOT NULL,
    estoque INT NOT NULL,
    vendas BIGINT NOT NULL
);

-- Inserção dos dados (exemplo)
INSERT INTO produtos (nome, categoria, marca, preco, estoque, vendas)
VALUES
    ('Calça Jeans Feminina Skinny', 'Calça', 'SHEIN BASICS', 129.90, 120, 10500),
    ('Calça Cargo Masculina', 'Calça', 'SHEIN MAN', 159.99, 85, 8700),
    ('Camisa Social Slim', 'Camisa', 'SHEIN MODA', 119.90, 200, 9400),
    ('Camisa Oversized Estampada', 'Camisa', 'SHEIN X', 99.90, 150, 8800),
    ('Vestido Midi Floral', 'Roupas', 'SHEIN ELEGANCE', 189.99, 95, 12000),
    ('Jaqueta Jeans Unissex', 'Roupas', 'SHEIN URBAN', 219.90, 60, 7600),
    ('Blusa Cropped Feminina', 'Roupas', 'SHEIN BASICS', 89.99, 170, 9900),
    ('Smartwatch SHEIN Fit', 'Eletrônicos', 'SHEIN TECH', 299.90, 50, 4500),
    ('Fone Bluetooth SHEIN Sound', 'Eletrônicos', 'SHEIN TECH', 189.90, 80, 5200),
    ('Mini Ring Light Portátil', 'Eletrônicos', 'SHEIN GADGETS', 99.90, 40, 6800);
