CREATE TABLE books(id INTEGER PRIMARY KEY, name TEXT, rating INTEGER);
INSERT INTO books VALUES(1,"Eleven Minutes",7);
INSERT INTO books VALUES(2,"The Kite Runner",9);
INSERT INTO books VALUES(3,"The Great Gatsby",8);
SELECT * FROM books




CREATE TABLE movies (id INTEGER PRIMARY KEY, name TEXT, release_year INTEGER);
INSERT INTO movies VALUES (1, "Avatar", 2009);
INSERT INTO movies VALUES (2, "Titanic", 1997);
INSERT INTO movies VALUES (3, "Star Wars: Episode IV - A New Hope", 1977);
INSERT INTO movies VALUES (4, "Shrek 2", 2004);
INSERT INTO movies VALUES (5, "The Lion King", 1994);
INSERT INTO movies VALUES (6, "Disney's Up", 2009);
SELECT * FROM movies;
SELECT * FROM movies WHERE release_year > 2000 ORDER BY release_year ; 




CREATE TABLE todo_list (id INTEGER PRIMARY KEY, item TEXT, minutes INTEGER);
INSERT INTO todo_list VALUES (1, "Wash the dishes", 15);
INSERT INTO todo_list VALUES (2, "vacuuming", 20);
INSERT INTO todo_list VALUES (3, "Learn some stuff on KA", 30);
INSERT INTO todo_list VALUES(4, "Go grocery shopping", 45);
SELECT SUM(minutes) FROM todo_list;




CREATE TABLE bikes(id INTEGER PRIMARY KEY, name TEXT, colour TEXT, price INTEGER, year_of_manufacture INTEGER );
INSERT INTO bikes VALUES(1,"KTM Duke","white",100000,2016);
INSERT INTO bikes VALUES(2,"YAMAHA RX","maroon",50000,2000);
INSERT INTO bikes VALUES(3,"ROYAL ENFIELD","red",150000,2018);
INSERT INTO bikes VALUES(4,"ACTIVA 5G","yellow",60000,2017);
INSERT INTO bikes VALUES(5,"ACCESS 125","black",70000,2019);
INSERT INTO bikes VALUES(6,"SCOOTY STREAK","pink",40000,2011);
INSERT INTO bikes VALUES(7,"abc","maroon",80000,2015);
INSERT INTO bikes VALUES(8,"RX","brown",30000,2016);
INSERT INTO bikes VALUES(9,"YAMAHA","blue",50000,2012);
INSERT INTO bikes VALUES(10,"XYZ","maroon",190000,2016);
INSERT INTO bikes VALUES(11,"HGF","orange",120000,2017);
INSERT INTO bikes VALUES(12,"GHB","maroon",670000,2001);
INSERT INTO bikes VALUES(13,"JHK","maroon",50000,2002);
INSERT INTO bikes VALUES(14,"HELL","majenta",560000,2003);
INSERT INTO bikes VALUES(15,"YESS","inkblue",780000,2004);
SELECT * FROM bikes;
SELECT id,price FROM bikes ORDER BY price;