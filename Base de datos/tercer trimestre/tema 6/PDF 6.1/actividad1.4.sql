SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_4;
create database actividad1_4;
use actividad1_4;


drop function if exists  mayusculas;

delimiter $$

create function mayusculas (
 arg1 varchar(50),
 arg2 varchar(50)
) returns varchar(101) 
begin
declare resultado varchar(101);
set resultado= concat (upper(arg1), '-', upper (arg2));
return resultado;
end $$

delimiter ;

select mayusculas ('Pepe', 'Luis');


