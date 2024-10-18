create database LaptopInfo;

use LaptopInfo;

create table laptop
(
	id int primary key auto_increment,
	SINo varchar(100) not null,
	Model varchar(10) not null,
	Brand varchar(100) not null,
	Price varchar(20) not null
);

insert into laptop(SINo, Model, Brand, Price) values('ABCD','ThinkPad', 'Dell', 50000);
insert into laptop(SINo, Model, Brand, Price) values('XYZA','Lenovo2', 'Lenovo', 60000)
