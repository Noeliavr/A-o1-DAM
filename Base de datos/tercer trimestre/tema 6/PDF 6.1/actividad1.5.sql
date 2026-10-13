drop database if exists actividad1_5;
create database actividad1_5;
use actividad1_5;


drop table if exists pagos;

create table pagos (
nombre varchar(100) not null primary key, 
cantidad numeric (5,2) not null);

insert into pagos (
nombre,
cantidad)
values
('Luis', 200),
('Luisa', 400),
('Enrique', 100),
('Ana', 400),
('Mónica', 300);



drop procedure if exists  pagos;

delimiter $$

create procedure pagos (
IN pago numeric (5,2)
) 
begin
select * from
pagos pa
where pa.cantidad >=pago;

end $$

delimiter ;

call pagos(200);


