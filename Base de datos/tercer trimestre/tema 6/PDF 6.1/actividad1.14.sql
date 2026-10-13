
drop database if exists actividad1_14;
create database actividad1_14;
use actividad1_14;


drop procedure if exists mostrarPares;

delimiter $$

create procedure mostrarTablas ()

begin

  declare contador1 numeric(2);
  declare contador2 numeric(2);
  declare producto numeric (2);
  declare resultado varchar (200);

  set contador1 = 0;
  set contador2 = 0;
  set producto = 0;
  set resultado = '';

  while contador1 <= 9 do

    set contador2 = 0;
    set resultado = '';

    while contador2 <= 9 do

      set producto = contador1*contador2;

      set resultado = concat (resultado, contador1, ' X ' , contador2, ' = ', producto, ', ');

      set contador2=contador2+1;

    end while;

    select resultado;
    set contador1=contador1+1;

  end while;

end $$

delimiter ;

call mostrarTablas();


