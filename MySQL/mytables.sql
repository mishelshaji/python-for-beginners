create database db_python;
use db_python;
create table stock(
	id int auto_increment primary key,
	item varchar(50),
	price numeric(10,2)
);
insert into stock(item,price) values('book',50);
insert into stock(item,price) values('bag',400);
insert into stock(item,price) values('pen',25);
select * from stock;