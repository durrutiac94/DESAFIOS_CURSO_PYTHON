#1. Crea el modelo (revisa bien cuál es el tipo de relación antes de crearlo), respeta las
claves primarias, foráneas y tipos de datos.

CREATE TABLE peliculas(id int primary key, nombre varchar(255), anno int);

CREATE TABLE tags(id int primary key, tag varchar(32));

CREATE TABLE peliculas_tags(id_pelicula int REFERENCES peliculas(id), id_tag int REFERENCES tags(id));

#2. Inserta 5 películas y 5 tags, la primera película tiene que tener 3 tags asociados, la
segunda película debe tener dos tags asociados.p

INSERT INTO peliculas VALUES (1, 'el senor de los anillos', 2001);
INSERT INTO peliculas VALUES (2, 'matrix', 1999);
INSERT INTO peliculas VALUES (3, 'parasitos', 2019);
INSERT INTO peliculas VALUES (4, 'interestelar', 2014);
INSERT INTO peliculas VALUES (5, 'el padrino', 1972);

INSERT INTO tags VALUES(1, 'fantasia');
INSERT INTO tags VALUES(2, 'ciencia ficcion');
INSERT INTO tags VALUES(3, 'accion');
INSERT INTO tags VALUES(4, 'drama');
INSERT INTO tags VALUES(5, 'crimen');

INSERT INTO peliculas_tags VALUES(1,1);
INSERT INTO peliculas_tags VALUES(1,2);
INSERT INTO peliculas_tags VALUES(1,3);
INSERT INTO peliculas_tags VALUES(2,4);
INSERT INTO peliculas_tags VALUES(2,5);

#3. Cuenta la cantidad de tags que tiene cada película. Si una película no tiene tags debe
mostrar 0.

SELECT peliculas.nombre, COUNT(peliculas_tags.id_tag)
FROM peliculas
LEFT JOIN peliculas_tags ON peliculas.id = peliculas_tags.id_pelicula
GROUP BY peliculas.id, peliculas.nombre;



