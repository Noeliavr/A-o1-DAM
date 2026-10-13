drop database if exists actividad1_7;
create database actividad1_7;
use actividad1_7;


drop procedure if exists mayor;

delimiter $$

create procedure mayor (
IN valor1 varchar(100),
IN valor2 numeric (5,2)
) 
begin

  if valor1 > valor2 then

    select concat ('El mayor es ' , valor1);

  elseif valor1 < valor2 then

    select concat ('El mayor es ' , valor2);

  else 

    select 'son iguales';

  end if;

end $$

delimiter ;

call mayor (1,2);
call mayor (2,1);
call mayor (2,2);





