create table stock(
	id int primary key,
	item text,
	price numeric(10,2)
);
insert into stock values(1,'book',50);
insert into stock values(2,'bag',400);
insert into stock values(3,'pen',25);
select * from stock;