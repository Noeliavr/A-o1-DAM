drop database if exists actividad1_20;
create database actividad1_20;
use actividad1_20;

create table empleados (
    id int primary key,
    nombre varchar(100) not null,
    salario decimal(10,2) not null
);

create table empleados_auditoria (
    id int auto_increment primary key,
    empleado_id int,
    salario_antiguo decimal(10,2),
    salario_nuevo decimal(10,2),
    fecha timestamp default current_timestamp,
    constraint fk_empleados_auditoria foreign key (empleado_id) references empleados(id) on update cascade on delete cascade
);

delimiter $$

create procedure insertar_empleados_auditoria
(in v_empleado int,
 in v_salario_antiguo decimal (10,2),
 in v_salario_nuevo decimal (10,2))

begin

  insert into empleados_auditoria (
    empleado_id,
    salario_antiguo,
    salario_nuevo) 
  values 
  (v_empleado, v_salario_antiguo, v_salario_nuevo);

end $$

create trigger tg_insert_empleados 
after
insert 
on empleados
for each row
begin

  call insertar_empleados_auditoria
  (NEW.id,
   null,
   NEW.salario);

end $$

create trigger tg_update_empleados 
after
update 
on empleados
for each row
begin

  call insertar_empleados_auditoria
  (NEW.id,
   OLD.salario,
   NEW.salario);

end $$


delimiter ;



insert into empleados (
id,
nombre,
salario
)
values 
(1, 'Pepe', 40000);

update empleados
set salario=42000
where id=1;

update empleados
set salario=44000
where id=1;

select * from empleados_auditoria;


