#4. Crea las tablas respetando los nombres, tipos, claves primarias y foráneas y tipos de
datos.
CREATE DATABASE requerimiento2;

CREATE TABLE preguntas(id int primary key, pregunta varchar(255), respuesta_correcta varchar);

CREATE TABLE usuarios(id int primary key, nombre varchar(255), edad int);

CREATE TABLE respuestas(id int primary key, respuesta varchar(255), 
usuario_id int REFERENCES usuarios(id), pregunta_id int REFERENCES preguntas(id));

#5. Agrega 5 registros a la tabla preguntas, de los cuales: (1 punto)
a. 1. La primera pregunta debe ser contestada correctamente por dos usuarios
distintos
b. 2. La pregunta 2 debe ser contestada correctamente por un usuario.
c. 3. Los otros dos registros deben ser respuestas incorrectas.

INSERT INTO usuarios VALUES(1, 'seba', 30);
INSERT INTO usuarios VALUES(2, 'valeska', 89);
INSERT INTO usuarios VALUES(3, 'maria', 40);
INSERT INTO usuarios VALUES(4, 'laura', 50);
INSERT INTO usuarios VALUES(5, 'mauricio', 60);

INSERT INTO preguntas VALUES(1, 'color del cielo', 'celeste');
INSERT INTO preguntas VALUES(2, 'color del sol', 'amarillo');
INSERT INTO preguntas VALUES(3, 'color del agua', 'transparente');
INSERT INTO preguntas VALUES(4, 'color de la tierra', 'cafe');
INSERT INTO preguntas VALUES(5, 'color del mar', 'azul');

INSERT INTO respuestas VALUES(1, 'celeste', 1, 1);
INSERT INTO respuestas VALUES(2, 'celeste',2,1);
INSERT INTO respuestas VALUES(3, 'amarillo',3,2);
INSERT INTO respuestas VALUES(4, 'azul',4,3);
INSERT INTO respuestas VALUES(5, 'rojo',5,4);

#6. Cuenta la cantidad de respuestas correctas totales por usuario (independiente de la pregunta).
SELECT usuarios.nombre, SUM(
        CASE
            WHEN respuestas.respuesta = preguntas.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas FROM usuarios
LEFT JOIN respuestas ON usuarios.id = respuestas.usuario_id
LEFT JOIN preguntas ON respuestas.pregunta_id = preguntas.id
GROUP BY usuarios.id, usuarios.nombre;

#7. Por cada pregunta, en la tabla preguntas, cuenta cuántos usuarios tuvieron la respuesta correcta.
SELECT preguntas.pregunta, SUM(
        CASE
            WHEN respuestas.respuesta = preguntas.respuesta_correcta THEN 1
            ELSE 0
        END
    ) AS respuestas_correctas FROM preguntas
LEFT JOIN respuestas
    ON preguntas.id = respuestas.pregunta_id
LEFT JOIN usuarios
    ON respuestas.usuario_id = usuarios.id
GROUP BY preguntas.pregunta;

#8. Implementa borrado en cascada de las respuestas al borrar un usuario y borrar el primer usuario para probar la implementación.
ALTER TABLE respuestas DROP CONSTRAINT respuestas_usuario_id_fkey, ADD FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE;
DELETE FROM usuarios WHERE id=1;

#9. Crea una restricción que impida insertar usuarios menores de 18 años en la base de datos.
ALTER TABLE usuarios ADD CONSTRAINT edad CHECK (edad>18);
INSERT INTO usuarios VALUES(6, 'camila', 17);

#10. Altera la tabla existente de usuarios agregando el campo email con la restricción de único.
ALTER TABLE usuarios ADD COLUMN email varchar UNIQUE;

