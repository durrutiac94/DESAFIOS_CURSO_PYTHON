CREATE TABLE clientes (
    email VARCHAR(50),
    nombre VARCHAR,
    telefono VARCHAR(16),
    empresa VARCHAR(50),
    prioridad SMALLINT
);

INSERT INTO clientes (email, nombre, telefono, empresa, prioridad) VALUES
('cliente1@mail.com', 'Ana Silva', '987654321', 'Lider', 1),
('cliente2@mail.com', 'Pedro Gomez', '912345678', 'Jumbo', 2),
('cliente3@mail.com', 'Maria Lopez', '998877665', 'Lider', 5),
('cliente4@mail.com', 'Juan Perez', '911223344', 'Unimarc', 8),
('cliente5@mail.com', 'Luis Torres', '955443322', 'Santa Isabel', 10);
