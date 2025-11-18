drop database if exists pokemon;
create database pokemon;
use pokemon;

create table tipos(
	id_tipo int auto_increment primary key,
	nombre_tipo varchar (20)
);

create table categorias(
	id_categoria int auto_increment primary key,
    nombre_categoria varchar (30)
);

create table pokemones(
	id_pokemon int auto_increment primary key,
    nombre varchar (30),
	numero_pokedex int,
    tipo1 int,
    tipo2 int,
    categoria int,
    foreign key (tipo1) references tipos (id_tipo),
    foreign key (tipo2) references tipos (id_tipo),
    foreign key (categoria) references categorias (id_categoria)
);

insert into tipos (nombre_tipo) values
	('Normal'),
	('Fuego'),
	('Agua'),
	('Planta'),
	('Eléctrico'),
	('Hielo'),
	('Lucha'),
	('Veneno'),
	('Tierra'),
	('Volador'),
	('Psíquico'),
	('Bicho'),
	('Roca'),
	('Fantasma'),
	('Dragón'),
	('Siniestro'),
	('Acero'),
	('Hada');

insert into categorias(nombre_categoria) values
	("mitico"),
	("legendario mayor"),
	("legendario menor"),
	("pseudolegendario"),
	("muy raro"),
	("normal");

insert into pokemones (nombre, numero_pokedex, tipo1, tipo2, categoria) values
	('Bulbasaur', 1, 4, 8, 6),
	('Charmander', 4, 2, null, 6),
	('Squirtle', 7, 3, null, 6),
	('Pikachu', 25, 5, null, 6),
	('Jigglypuff', 39, 1, 18, 6),
	('Machop', 66, 7, null, 6),
	('Gastly', 92, 14, 8, 6),
	('Geodude', 74, 13, 9, 6),
	('Onix', 95, 13, 9, 6),
	('Eevee', 133, 1, null, 6),
	('Chikorita', 152, 4, null, 6),
	('Cyndaquil', 155, 2, null, 6),
	('Totodile', 158, 3, null, 6),
	('Mareep', 179, 5, null, 6),
	('Hoothoot', 163, 1, 10, 6),
	('Heracross', 214, 12, 7, 5),
	('Sneasel', 215, 16, 6, 6),
	('Steelix', 208, 17, 9, 5),
	('Togetic', 176, 18, 10, 5),
	('Espeon', 196, 11, null, 6),
	('Treecko', 252, 4, null, 6),
	('Torchic', 255, 2, null, 6),
	('Mudkip', 258, 3, null, 6),
	('Ralts', 280, 11, 18, 6),
	('Aron', 304, 17, 13, 6),
	('Trapinch', 328, 9, null, 6),
	('Swablu', 333, 1, 10, 6),
	('Spheal', 363, 6, 3, 6),
	('Absol', 359, 16, null, 5),
	('Flygon', 330, 9, 15, 4),
	('Turtwig', 387, 4, null, 6),
	('Chimchar', 390, 2, null, 6),
	('Piplup', 393, 3, null, 6),
	('Shinx', 403, 5, null, 6),
	('Lucario', 448, 7, 17, 5),
	('Gible', 443, 15, 9, 4),
	('Snivy', 495, 4, null, 6),
	('Tepig', 498, 2, null, 6),
	('Oshawott', 501, 3, null, 6),
	('Zorua', 570, 16, null, 5),
	('Fennekin', 653, 2, null, 6),
	('Froakie', 656, 3, null, 6),
	('Gogoat', 673, 4, null, 6),
	('Rowlet', 722, 4, 10, 6),
	('Litten', 725, 2, null, 6),
	('Popplio', 728, 3, null, 6),
	('Mimikyu', 778, 14, 18, 5);
