drop database if exists actividad1_1;
create database actividad1_1;
use actividad1_1;


drop procedure if exists mostrarVersion ;

delimiter $$

create procedure mostrarVersion ()
begin
select version();
end $$

delimiter ;

call mostrarVersion();

