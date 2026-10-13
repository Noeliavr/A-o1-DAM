drop database if exists actividad1_19;
create database actividad1_19;
use actividad1_19;

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




drop procedure if exists  gestionar_reserva;

delimiter $$

create procedure gestionar_reserva (
IN id_cliente int,
IN numero_habitacion numeric(3,0), 
IN fecha_inicio date,
IN fecha_fin date,
OUT resultadoOK boolean,
OUT mensaje_error varchar(100)
) 
begin

DECLARE v_saldo_cliente_actual NUMERIC (10,2) DEFAULT NULL;
DECLARE v_precio_habitacion NUMERIC (6,2) DEFAULT NULL;
DECLARE v_numero_dias NUMERIC (3,0) DEFAULT NULL;

#si algo falla hacemos rollback
declare exit handler for SQLEXCEPTION rollback;

SET resultadoOK=TRUE;
SET mensaje_error=NULL;

START TRANSACTION;

#Comprobamos fechas correctas
if NOT fecha_fin > fecha_inicio OR fecha_inicio < curdate() then
	SET resultadoOK=FALSE;
	SET mensaje_error='Fechas incorrectas';

ELSE
	set v_numero_dias=datediff(fecha_fin,fecha_inicio);
END if;

#Obtenemos precio habitacion y validamos que exista
if resultadoOK = TRUE then
	SELECT ha.precio_noche INTO v_precio_habitacion
	FROM habitaciones ha
	WHERE ha.numero_habitacion=numero_habitacion;

	if v_precio_habitacion IS NULL then
	
		SET resultadoOK=FALSE;
		SET mensaje_error='Habitación no existe';
	
	END if;
END if;


#Obtenemos saldo cliente y validamos que exista
if resultadoOK = TRUE then

	SELECT cl.saldo INTO v_saldo_cliente_actual
	FROM clientes cl
	WHERE cl.id_cliente=id_cliente
	FOR UPDATE;

	if v_saldo_cliente_actual IS NULL then
	
		SET resultadoOK=FALSE;
		SET mensaje_error='Cliente no existe';
		
	END if;

END if;

#Comprobamos que tenga saldo
if resultadoOK = TRUE then

	if v_saldo_cliente_actual < v_numero_dias*v_precio_habitacion then
	
		SET resultadoOK=FALSE;
		SET mensaje_error='Cliente no tiene suficiente saldo';
		
	END if;

END if;


if resultadoOK = TRUE then

	INSERT INTO reservas (
	id_cliente,
	numero_habitacion,
	fecha_entrada,
	fecha_salida
	) VALUES (
	id_cliente,
	numero_habitacion,
	fecha_inicio,
	fecha_fin
	);

	UPDATE clientes cl
	SET cl.saldo=cl.saldo-v_numero_dias*v_precio_habitacion
	WHERE cl.id_cliente=id_cliente;

end if;

if resultadoOK = TRUE then
	COMMIT;
ELSE
	ROLLBACK;
END if;


end $$

delimiter ;


CALL gestionar_reserva(1, 301, 20260603, 20260602, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL gestionar_reserva(1, 301, curdate()-1, 20260603, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL gestionar_reserva(1, 301, 20260601, 20260603, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL gestionar_reserva(1, 302, 20260601, 20260603, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL gestionar_reserva(2, 301, 20260601, 20260603, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL gestionar_reserva(1, 201, 20260601, 20260603, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;


