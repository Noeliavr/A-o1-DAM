SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_16;
create database actividad1_16;
use actividad1_16;


drop function if exists validaIntervalo;
drop function if exists esPrimo;
drop procedure if exists rellenarPrimos;
drop table if exists numeros_primos;

create table numeros_primos ( 
numero numeric (5,2) not null primary key);


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


create function esPrimo (
 numero numeric (3)
) returns numeric (1)
begin

  declare resultado numeric (1);
  declare contador numeric (3);

  set resultado=1;

   if numero > 2 then

    set contador = numero - 1;


    repeat 

      if numero mod contador = 0 then
       
	#No es primo
        set contador=1;
        set resultado=0;

      else

        
	#puede ser primo, seguimos buscando
        set contador = contador - 1;

      end if; 

    until contador=1
    end repeat;

  ELSEif numero <= 0 then

    set resultado=0;

  end if;


return resultado;

end $$

create procedure rellenarPrimos
(in limiteInferior numeric (6),
 in limiteSuperior numeric (6)
) 
begin

  declare contador numeric (6);

  set contador = limiteInferior;

  if validaIntervalo (limiteInferior, limiteSuperior) = 1 then

    delete from numeros_primos;

    while contador <= limiteSuperior do

      if esPrimo (contador) then

        insert into numeros_primos values (contador);

      end if;

      set contador = contador + 1;

    end while;

  end if;



end $$

delimiter ;

call rellenarPrimos (5, 27);
select * from numeros_primos;


