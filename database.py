products_db="""
CREATE TABLE IF NOT EXISTS products (
ID int not null AUTO_INCREMENT,
name varchar(255) not null,
price float,
primary key(ID)
);"""

couriers_db="""
CREATE TABLE IF NOT EXISTS couriers (
ID int not null AUTO_INCREMENT,
name varchar(255) ,
phone int,
primary key(ID)
);"""

customers_db="""
CREATE TABLE IF NOT EXISTS customers(
ID int not null AUTO_INCREMENT ,
customer_name varchar(255),
customer_address varchar(255),
customer_phone varchar(255),
primary key(ID)
);"""

orders_db="""
CREATE TABLE IF NOT EXISTS orders(
ID int not null AUTO_INCREMENT ,
customer_ID int not null,
foreign key (customer_ID) references customers(ID), 
courier_ID int not null,
foreign key (courier_ID) references couriers(ID),
status varchar(255),
product_ID varchar(255),
primary key(ID)
);"""

productorders_db="""
CREATE TABLE IF NOT EXISTS productorders (
order_ID int ,
foreign key (order_ID) references orders(ID),
product_ID int ,
foreign key (product_ID) references products(ID)
);"""
