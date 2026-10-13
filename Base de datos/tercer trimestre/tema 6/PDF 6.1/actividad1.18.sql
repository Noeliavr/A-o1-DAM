drop database if exists actividad1_18;
create database actividad1_18;
use actividad1_18;

create table clientes (
    id_cliente int primary key,
    nombre     varchar(50) not null,
    saldo      numeric(10,2) not null
);

create table productos (
    id_producto int primary key,
    nombre      varchar(50) not null,
    precio      numeric (5,2) not null,
    stock       int not null,
constraint chk_stock check (stock >=0)
);

create table pedidos (
    id_pedido    int auto_increment primary key,
    id_cliente   int not null,
    fecha_hora   datetime not null,
    constraint fk_cliente foreign key (id_cliente)
        references clientes(id_cliente)
);

create table detalle_pedidos (
    id_pedido    int not null,
    id_producto  int not null,
    cantidad     int not null,
    constraint pk_detalles_pedidos primary key (id_pedido, id_producto),
    constraint fk_pedido foreign key (id_pedido)
        references pedidos(id_pedido),
    constraint fk_producto foreign key (id_producto)
        references productos(id_producto)
);

insert into clientes VALUES (1, 'Ana', 1000);
insert into clientes VALUES (2, 'Luis', 500);

insert into productos VALUES (1, 'Teclado', 50, 10);
insert into productos VALUES (2, 'Ratón', 10, 20);
insert into productos VALUES (3, 'Monitor', 200, 5);



drop procedure if exists  procesar_pedido;

delimiter $$

create procedure procesar_pedido (
IN id_cliente int,
IN id_producto int, 
IN cantidad int,
OUT resultadoOK boolean,
OUT mensaje_error varchar(100)
) 
begin

DECLARE v_stock_actual INT DEFAULT null;
DECLARE v_precio_producto INT DEFAULT null;
DECLARE v_saldo_cliente_actual INT DEFAULT NULL;
DECLARE v_pedido INT DEFAULT NULL;

#si algo falla hacemos rollback
declare exit handler for SQLEXCEPTION rollback;

SET resultadoOK=TRUE;
SET mensaje_error=NULL;


if cantidad < 0 then
	set resultadoOK=FALSE;
	set mensaje_error='Cantidad no puede ser negativa';
END if;


START TRANSACTION;

if resultadoOK = TRUE then
	SELECT pr.stock, pr.precio INTO v_stock_actual, v_precio_producto
	FROM productos pr
	WHERE pr.id_producto=id_producto
	FOR UPDATE;
	
	if v_stock_actual is null or cantidad > v_stock_actual then
		set resultadoOK=FALSE;
		set mensaje_error='No hay suficiente stock';
	END if;
END if;

if resultadoOK = TRUE then
	SELECT saldo INTO v_saldo_cliente_actual
	FROM clientes cl
	WHERE cl.id_cliente=id_cliente
	FOR UPDATE;
	
	if v_saldo_cliente_actual is null or v_precio_producto*cantidad > v_saldo_cliente_actual then
		set resultadoOK=FALSE;
		set mensaje_error='Cliente no tiene suficiente saldo';
	END if;
END if;

if resultadoOK = TRUE then

	INSERT INTO pedidos (
	id_cliente,
	fecha_hora) 
	VALUES (
	id_cliente,
	NOW());
	
	SET v_pedido=LAST_INSERT_ID();
	
	INSERT INTO detalle_pedidos (
	id_pedido,
	id_producto,
	cantidad)
	VALUES (
	v_pedido,
	id_producto,
	cantidad);
	
	UPDATE productos pr
	SET pr.stock = pr.stock-cantidad
	WHERE pr.id_producto=id_producto;
	
	UPDATE clientes cl
	SET cl.saldo=cl.saldo - v_precio_producto*cantidad
	WHERE cl.id_cliente=id_cliente;


END if;



if resultadoOK = TRUE then
	COMMIT;
ELSE
	ROLLBACK;
END if;

end $$

delimiter ;


CALL procesar_pedido(1, 1, 3, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL procesar_pedido(2, 3, 2, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL procesar_pedido(2, 2, 10, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;

CALL procesar_pedido(2, 2, 1, @resultadoOK, @mensaje_error);
 select @resultadoOK, @mensaje_error;


