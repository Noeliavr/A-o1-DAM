drop database if exists actividad1_17;
create database actividad1_17;
use actividad1_17;


create table empleados (
    id int primary key auto_increment,
    nombre varchar(100),
    salario decimal(10,2),
    departamento varchar(50)
);

insert into empleados (nombre, salario, departamento) values
('Ana', 1200, 'Ventas'),
('Luis', 1500, 'IT'),
('Marta', 1100, 'Ventas'),
('Carlos', 2000, 'IT'),
('Elena', 1300, 'Marketing');


delimiter $$

create procedure procActualizar ()
begin

  declare v_id int;
  declare v_salario decimal(10,2);
  declare v_departamento varchar(50);
  declare fin_consulta BOOL default 0;

  #declaracion cursor
  declare miCursor CURSOR FOR 
  select id, salario, departamento
  from empleados;

  #declaración fin de consulta
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET fin_consulta = 1; 
  set fin_consulta=0;

  #abrimos el cursor
  OPEN miCursor;

  loopcursor: LOOP
  
    FETCH miCursor into v_id, v_salario, v_departamento;
    if fin_consulta = 1 then
       LEAVE loopcursor;
    end if;
  
    if v_departamento = 'Ventas' then
      set v_salario = v_salario*1.1;
    elseif v_departamento = 'IT' then
      set v_salario = v_salario*1.05;
    else 
      set v_id = null;
    end if;
  
    if v_id is not null then
  
      update empleados
      set salario=v_salario
      where id=v_id;
  
    end if;
  
  
  end loop loopcursor;

  CLOSE miCursor;

end $$

delimiter ;


select * from empleados;
call procActualizar ;
select * from empleados;



