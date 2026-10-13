SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_12;
create database actividad1_12;
use actividad1_12;


drop function if exists validaIntervalo;
drop procedure if exists mostrarPares;

delimiter $$

create function validaIntervalo (
 limiteInferior numeric (6),
 limiteSuperior numeric (6)
) returns numeric (1)
begin

  declare resultado numeric (1) default 0;

  if limiteInferior >= 0 and limiteSuperior >=0 and limiteInferior < limiteSuperior then

    set resultado = 1;

  end if;

return resultado;

end $$

create procedure mostrarPares (
 limiteInferior numeric (6),
 limiteSuperior numeric (6))

begin

  declare contador numeric(6);
  declare resultado varchar (100);

  set contador = limiteInferior;
  set resultado = '';

  if validaIntervalo(limiteInferior, limiteSuperior) = 1 then

    while contador <= limiteSuperior do

      if contador mod 2 = 0 then
      
        set resultado = concat (resultado, contador, ', ');

      end if;

      set contador = contador + 1;

    end while;

    select resultado;

  else

    select 'Error, limiteInferior y limiteSuperior deben ser positivos y limiteInferior menor que limiteSuperior';

  end if;

end $$

delimiter ;

call mostrarPares(4,4);
call mostrarPares(4,3);
call mostrarPares(-4,-2);
call mostrarPares(-1,2);
call mostrarPares(4,6);


