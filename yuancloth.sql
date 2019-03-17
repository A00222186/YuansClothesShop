CREATE DATABASE IF NOT EXISTS yuanshop;
USE yuanshop;

DROP TABLE IF EXISTS USERTABLE;

CREATE TABLE USERTABLE(
	userid int auto_increment primary key,
    username varchar(100) not null,
    userpassword varchar(100) not null,
    birthday date,
    gender varchar(40),
    permission varchar(40),
    statustype varchar(40)
   
);


DROP TABLE IF EXISTS PRODUCT;
CREATE TABLE PRODUCT(
	productid int auto_increment primary key,
    gender varchar(40),
    age int,
    producttype varchar(40),
    productsize varchar(100),
    price double,
    stock int
);



DROP TABLE IF EXISTS SHOPCART;

CREATE TABLE SHOPCART(
	cartid int auto_increment primary key,
    productid int,
    userid int,
	quantity int,
    foreign key (productid) references PRODUCT(productid),
    foreign key (userid) references USERTABLE(userid)
);


insert into usertable values(null,'yuan','123456','1996-3-8','male','admin','available');
insert into usertable values(null,'xi','123456','1999-8-3','female','admin','available');
insert into usertable values(null,'yuxin','123456','1996-4-7','male','admin','available');
insert into usertable values(null,'nama','123456','1997-6-7','male','admin','available');
insert into usertable values(null,'shwetank','123456','1998-2-10','male','admin','available');
insert into usertable values(null,'jhon','654321','1996-10-10','male','manager','available');
insert into usertable values(null,'ash','123456','1999-7-18','female','user','available');

select * from usertable;
select * from product;


insert into product values(null,'female',18,'cloth','S',18.8,100);
insert into product values(null,'male',20,'cloth','XL',20.99,88);
insert into product values(null,'male',20,'cloth','XXL',27.99,81);
insert into product values(null,'female',20,'cloth','M',21.99,85);
insert into product values(null,'male',20,'cloth','S',22.99,58);
insert into product values(null,'male',22,'cloth','XL',25.99,78);
insert into product values(null,'male',22,'shoes','9',25.99,78);
insert into product values(null,'male',22,'T-shirt','XL',235.99,100);
