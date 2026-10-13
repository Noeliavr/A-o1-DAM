SET GLOBAL log_bin_trust_function_creators=1;

drop database if exists actividad1_15;
create database actividad1_15;
use actividad1_15;


drop function if exists esPrimoFunc;

delimiter $$

create function esPrimoFun (
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

delimiter ;

select esPrimoFun(1);
select esPrimoFun(2);
select esPrimoFun(3);
select esPrimoFun(7);
select esPrimoFun(8);
select esPrimoFun(0);
select esPrimoFun(-4);


