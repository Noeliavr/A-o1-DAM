SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_3;
create database actividad1_3;
use actividad1_3;


drop function if exists  saluda;

delimiter $$

create function saluda (
 nombre varchar(50)
) returns varchar(50) 
begin
declare resultado varchar(50);
set resultado= concat ('Hola ', nombre);
return resultado;
end $$

delimiter ;

select saluda ('Pepe');


