drop database if exists actividad1_6;
create database actividad1_6;
use actividad1_6;


drop table if exists pagos;

create table pagos (
nombre varchar(100) not null primary key, 
cantidad numeric (5,2) not null);

insert into pagos (
nombre,
cantidad)
values
('Luis', 200),
('Luisa', 400),
('Enrique', 100),
('Ana', 400),
('Mónica', 300);



drop procedure if exists  pagos;

delimiter $$

create procedure pagos (
IN nombre varchar(100),
IN cantidad numeric (5,2)
) 
begin

  insert into pagos (
  nombre, 
  cantidad) 
  values (
  nombre,
  cantidad);

end $$

delimiter ;

call pagos('Pepe',200);

select * from pagos;




