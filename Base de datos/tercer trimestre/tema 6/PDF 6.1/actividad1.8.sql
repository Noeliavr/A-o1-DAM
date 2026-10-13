drop database if exists actividad1_8;
create database actividad1_8;
use actividad1_8;


drop procedure if exists nota;

delimiter $$

create procedure nota (
IN nota numeric (3,2)
) 
begin

  if nota >=0 and nota < 5 then

    select 'Insuficiente';

  elseif nota >=5 and nota < 6 then

    select 'Suficiente';

  elseif nota >=6 and nota < 7 then

    select 'Bien';

  elseif nota >=7 and nota < 9 then

    select 'Notable';

  elseif nota >=9 and nota <= 10 then

    select 'Sobresaliente';

  else

    select 'Nota no válida';

  end if;

end $$

delimiter ;

call nota (1);
call nota (5);
call nota (6);
call nota (7);
call nota (9);
call nota (-1);






