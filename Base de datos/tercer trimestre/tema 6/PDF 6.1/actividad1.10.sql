drop database if exists actividad1_10;
create database actividad1_10;
use actividad1_10;


drop procedure if exists quiniela;

delimiter $$

create procedure quiniela (
IN goles_local numeric (2),
IN goles_visitante numeric (2)
) 
begin

  if goles_local >=0 and goles_visitante >= 0 then

    if goles_local > goles_visitante then

      select '1';

    elseif goles_local < goles_visitante then

      select '2';

    else

      select 'X';

    end if;

  else

    select 'resultado no válido';

  end if;

end $$

delimiter ;

call quiniela (1,1);
call quiniela (2,1);
call quiniela (1,3);
call quiniela (-1,2);






