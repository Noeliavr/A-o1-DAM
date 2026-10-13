drop database if exists actividad1_2;
create database actividad1_2;
use actividad1_2;


drop procedure if exists  saluda;

delimiter $$

create procedure saluda (
IN nombre varchar(50)
) 
begin
select concat ('Hola ', nombre);
end $$

delimiter ;

call saluda('Pepe');

