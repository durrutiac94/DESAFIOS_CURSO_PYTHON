CREATE TABLE clientes (
    email varchar(50),
    nombre varchar,
    telefono varchar(16),
    empresa varchar(50),
    prioridad smallint
);

INSERT INTO 
clientes 
VALUES
('abc@gmail.com','abc','123456789','qwerty',10),
('def@gmail.com','def','987654321','asdf',9),
('ghj@gmail.com','ghj','123123133','jsjsj',5),
('jkl@gmail.com','abc','919191919','aaalala',1),
('zxc@gmail.com','zxc','828282828','qwerty',2);


SELECT * FROM clientes;

SELECT * FROM clientes ORDER BY prioridad DESC LIMIT 3;
#ordenar por orden segun prioridad 
#limitar la cantidad de filas de la consulta 

SELECT * FROM clientes WHERE empresa = qwerty;