drop database if exists escuela;
create  database escuela;
use escuela;

create table Rubricas(
    id_rubrica int primary key auto_increment,
    nombre_rubrica varchar (40)
);


create table Criterios(
    id_criterio int primary key auto_increment,
    nombre_criterio varchar (40),
    nota float,
    nota_maxima int,
    rubrica int,
    foreign key (rubrica) references Rubricas(id_rubrica)
);
