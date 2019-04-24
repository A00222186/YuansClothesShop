-- #---manager----
-- create user 'manager'@'localhost' identified by 'manager';

-- grant select, insert , update, delete on yuanshop.product to  'manager'@'localhost';


-- #------------------------------------------------------------------
-- create user 'user'@'localhost' identified by 'user';

-- grant select,update on yuanshop.product to 'user'@'localhost';
-- grant select,update,delete,insert on yuanshop.shopcart to 'user'@'localhost';


-- drop table if EXISTS visitor;
-- CREATE TABLE VISITOR(
--  id int auto_increment primary key,
--      visitornumber int default 0,
--         days int,
--     months int,
--     years int,
--      visitordate date  
-- );


--drop table loginvisitor;
--create table loginvisitor(
--	id int auto_increment primary key,
--    UserId int,
--    visitordate date,
--    FOREIGN KEY (UserId) REFERENCES USERTABLE(userid)
--);


-- SET SQL_SAFE_UPDATES = 0;

-- drop event  IF EXISTS  add_new_visitor;

-- create  event `add_new_visitor`
-- ON SCHEDULE EVERY 24 hour STARTS '2019-03-26 00:00:00'
-- ON COMPLETION NOT PRESERVE ENABLE
-- DO CALL `add_visitor`;

-- set GLOBAL event_scheduler = 1; 

-- ALTER EVENT add_new_visitor DISABLE;
--  
--  
-- ALTER EVENT add_new_visitor ENABLE;



#-----------------------------create procedures---------------------------

-- CREATE DEFINER=`root`@`localhost` PROCEDURE `add_visitor`()
-- BEGIN
--  declare mouths int;
--         declare years int;
--         declare days int;
--         declare visitordate date;
--  SELECT MONTH(NOW()) INTO mouths;
--         SELECT YEAR(now()) INTO years;
--         SELECT day(NOW()) INTO days;
--         SELECT CURDATE() INTO visitordate;
--  insert INTO VISITOR VALUE(NULL,0,days,mouths,years,visitordate);
--         
-- END




-- CREATE DEFINER=`root`@`localhost` PROCEDURE `get_week`()
-- BEGIN
-- declare months int;
-- SELECT MONTH(NOW()) INTO months;
-- select v.visitornumber,v.days,v.months,v.years from visitor v where DATE_SUB(CURDATE(), INTERVAL 6 DAY);
-- END




-- CREATE DEFINER=`root`@`localhost` PROCEDURE `update_visitor`()
-- BEGIN
-- declare nowdate date;
-- SELECT CURDATE() INTO nowdate;
-- UPDATE VISITOR SET visitornumber = visitornumber + 1 WHERE visitordate = nowdate ;

-- END

-- drop table loginvisitor;
-- create table loginvisitor(
-- 	id int auto_increment primary key,
--     UserId int,
--     visitordate date,
--     FOREIGN KEY (UserId) REFERENCES USERTABLE(userid)
-- );
-- insert into loginvisitor values(null,'1','2019-04-18');
-- insert into loginvisitor values(null,'2','2019-04-18');
-- insert into loginvisitor values(null,'3','2019-04-18');
-- insert into loginvisitor values(null,'4','2019-04-18');
-- insert into loginvisitor values(null,'5','2019-04-18');
-- insert into loginvisitor values(null,'6','2019-04-18');
-- insert into loginvisitor values(null,'7','2019-04-18');



-- insert into loginvisitor values(null,'1','2019-04-19');
-- insert into loginvisitor values(null,'2','2019-04-19');
-- insert into loginvisitor values(null,'3','2019-04-19');
-- insert into loginvisitor values(null,'4','2019-04-19');
-- insert into loginvisitor values(null,'5','2019-04-19');
-- insert into loginvisitor values(null,'6','2019-04-19');
-- insert into loginvisitor values(null,'7','2019-04-19');
-- insert into loginvisitor values(null,'8','2019-04-19');
-- insert into loginvisitor values(null,'9','2019-04-19');
-- insert into loginvisitor values(null,'10','2019-04-19');
-- insert into loginvisitor values(null,'11','2019-04-19');
-- insert into loginvisitor values(null,'12','2019-04-19');
-- insert into loginvisitor values(null,'13','2019-04-19');
-- insert into loginvisitor values(null,'14','2019-04-19');
-- insert into loginvisitor values(null,'15','2019-04-19');
-- insert into loginvisitor values(null,'16','2019-04-19');
-- insert into loginvisitor values(null,'17','2019-04-19');

-- insert into loginvisitor values(null,'1','2019-04-20');
-- insert into loginvisitor values(null,'2','2019-04-20');
-- insert into loginvisitor values(null,'3','2019-04-20');
-- insert into loginvisitor values(null,'4','2019-04-20');
-- insert into loginvisitor values(null,'5','2019-04-20');
-- insert into loginvisitor values(null,'6','2019-04-20');
-- insert into loginvisitor values(null,'7','2019-04-20');


-- create table soldproducts(
-- orderid int PRIMARY KEY auto_increment,
--     quantity int,
-- productid int,
--     name Varchar(45),
--     price int,
--     color Varchar(45),
--     curr_time timestamp default current_timestamp,
--     foreign key(productid) references product(productid));


-- create view test_view as
-- select shopcart.cartid, shopcart.quantity, product.productid, product.name, product.price, product.color, now()
-- from product, shopcart
-- where product.productid = shopcart.productid;

-- insert into shopcart values(1, 1, 1, 5)
