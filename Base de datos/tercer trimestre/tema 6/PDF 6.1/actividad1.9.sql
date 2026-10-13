drop database if exists actividad1_9;
create database actividad1_9;
use actividad1_9;


drop procedure if exists dia_semana;

delimiter $$

create procedure dia_semana (
IN dia_semana numeric (1)
) 
begin

  case dia_semana 

    when 1 then

      select 'Lunes';

    when 2 then

      select 'Martes';

    when 3 then

      select 'Miércoles';

    when 4 then

      select 'Jueves';

    when 5 then

      select 'Viernes';

    when 6 then

      select 'Sábado';

    when 7 then

      select 'Domingo';

    else

      select 'No válido';

  end case;

end $$

delimiter ;

call dia_semana (1);
call dia_semana (5);
call dia_semana (6);
call dia_semana (7);
call dia_semana (9);
call dia_semana (-1);






