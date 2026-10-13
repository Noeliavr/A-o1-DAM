SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_11;
create database actividad1_11;
use actividad1_11;


drop function if exists operar;

delimiter $$

create function operar (
 numero1 numeric (6),
 numero2 numeric (6),
 operacion numeric (1)
) returns numeric (12)
begin

  declare resultado numeric (12) default null;

  if operacion = 1 then

    set resultado = numero1 + numero2;

  elseif operacion = 2 then

    set resultado = numero1 - numero2;

  elseif operacion = 3 then

    set resultado = numero1 * numero2;

  elseif operacion = 4 then

    set resultado = numero1 / numero2;

  end if;

return resultado;

end $$

delimiter ;

select operar (4,2,1);
select operar (4,2,2);
select operar (4,2,3);
select operar (4,2,4);


