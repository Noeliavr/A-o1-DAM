drop database if exists actividad1_21;
create database actividad1_21;
use actividad1_21;

SET GLOBAL log_bin_trust_function_creators=1;

create table clientes (
    id_cliente int auto_increment primary key,
    nombre varchar(50) not null,
    saldo numeric(10,2) not null,
    constraint chk_saldo check (saldo >=0) 

);

create table habitaciones (
    numero_habitacion numeric (3,0) primary key,
    precio_noche numeric(6,2)
);

create table reservas (
    id_reserva int auto_increment primary key,
    id_cliente int not null,
    numero_habitacion numeric (3,0) not null,
    fecha_entrada date,
    fecha_salida date,
    foreign key (id_cliente) references clientes(id_cliente),
    foreign key (numero_habitacion) references habitaciones(numero_habitacion)
);


insert into clientes (nombre, saldo) values
('Carlos', 500),
('Marta', 150);

insert into habitaciones (numero_habitacion, precio_noche) values
(101, 100),
(201, 200),
(301, 300);



#Pruebas
#insert into reservas (
#id_cliente,
#numero_habitacion,
#fecha_entrada,
#fecha_salida)
#values (
#1,
#101,
#20260601,
#20260603);

#select *
#from reservas
#where (id_reserva is null or id_reserva!=1) and
#numero_habitacion=101 and
#fecha_entrada<=20260601 and 
#fecha_salida>20260601;
#
#
##Prueba
#select *
#from reservas
#where numero_habitacion=101 and
#fecha_entrada>=20260601 and 
#fecha_entrada<20260605;
#
#Pruebas
#set @v_habitacion=101;
#set @v_reserva=null;
#set @v_fecha_entrada=20260602;
#set @v_fecha_salida=20260604;
#set @v_resultado=null;
#select 1 
#from reservas
#where (@v_reserva is null or id_reserva!=@v_reserva) and
#numero_habitacion=@v_habitacion and
#fecha_entrada<=@v_fecha_entrada and 
#fecha_salida>@v_fecha_entrada
#union
#select 1 
#from reservas
#where (@v_reserva is null or id_reserva!=@v_reserva) and
#numero_habitacion=@v_habitacion and
#fecha_entrada>=@v_fecha_entrada and 
#fecha_entrada<@v_fecha_salida
#into @v_resultado;
#
#select @v_resultado;


delimiter $$

create function fechasOK (
v_id_reserva int,
v_numero_habitacion numeric (3,0),
v_fecha_entrada date,
v_fecha_salida date) 
returns numeric (1)
begin

  declare v_resultado numeric (1);
  set v_resultado = null;

  select 1 
  from reservas
  where (v_id_reserva is null or id_reserva!=v_id_reserva) and
  numero_habitacion=v_numero_habitacion and
  fecha_entrada<=v_fecha_entrada and 
  fecha_salida>v_fecha_entrada
  union
  select 1 
  from reservas
  where (v_id_reserva is null or id_reserva!=v_id_reserva) and
  numero_habitacion=v_numero_habitacion and
  fecha_entrada>=v_fecha_entrada and 
  fecha_entrada<v_fecha_salida
  into v_resultado;

  if v_resultado is null then
    set v_resultado=1;
  else
    set v_resultado=0;
  end if;

  return v_resultado;

end $$ 

create trigger tg_insert_reserva 
before
insert 
on reservas
for each row
begin

  declare v_resultado numeric(1) ;
  set v_resultado=1;

  set v_resultado= fechasOK (
    null,
    NEW.numero_habitacion,
    NEW.fecha_entrada,
    NEW.fecha_salida);

  if v_resultado = 0 then

    signal sqlstate '45000'
    set message_text = 'Ya existe reserva en esas fechas';

  end if;

end $$

create trigger tg_update_reserva 
before
update 
on reservas
for each row
begin

  declare v_resultado numeric(1) ;
  set v_resultado=1;

  set v_resultado= fechasOK (
    OLD.id_reserva,
    NEW.numero_habitacion,
    NEW.fecha_entrada,
    NEW.fecha_salida);

  if v_resultado = 0 then

    signal sqlstate '45000'
    set message_text = 'Ya existe reserva en esas fechas';

  end if;

end $$




delimiter ;


#select fechasOK(101,20260602,20260603);


insert into reservas (
id_cliente,
numero_habitacion,
fecha_entrada,
fecha_salida)
values (
1,
101,
20260601,
20260603);

insert into reservas (
id_cliente,
numero_habitacion,
fecha_entrada,
fecha_salida)
values (
1,
101,
20260602,
20260604);


insert into reservas (
id_cliente,
numero_habitacion,
fecha_entrada,
fecha_salida)
values (
1,
101,
20260603,
20260604);

update reservas
set fecha_entrada=20260604,
fecha_salida=20260605
where id_reserva=2;

update reservas
set fecha_entrada=20260602,
fecha_salida=20260603
where id_reserva=2;





