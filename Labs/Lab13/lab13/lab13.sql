.read data.sql


CREATE TABLE bluedog AS
  SELECT color AS color, pet AS pet FROM students
	 WHERE color = "blue" AND pet = "dog";

CREATE TABLE bluedog_songs AS
  SELECT color AS color, pet AS pet, song AS song FROM students
         WHERE color = "blue" AND pet = "dog";


CREATE TABLE smallest_int_having AS
  SELECT time AS time, smallest AS smallest FROM students
         GROUP BY smallest HAVING count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet AS pet, a.song AS song, a.color AS first_color, b.color AS second_color
         FROM students AS a, students AS b
	 WHERE a.pet = b.pet AND a.song = b.song AND a.time < b.time; 


CREATE TABLE sevens AS
  SELECT s.seven AS seven FROM students AS s, numbers AS n
         WHERE s.time = n.time AND s.number = 7 AND n."7" = "True"; 


CREATE TABLE average_prices AS
  SELECT category AS category, avg(MSRP) AS average_price
         FROM products GROUP BY category;


CREATE TABLE lowest_prices AS
  SELECT inv.store AS store, inv.item AS item, min(inv.price) as price
         FROM inventory AS inv GROUP BY item;

CREATE TABLE helper_list AS
  SELECT name AS item, min(MSRP / rating) FROM products
         GROUP BY category;

CREATE TABLE shopping_list AS
  SELECT hel.item AS item, low_pri.store AS store
         FROM helper_list AS hel, lowest_prices AS low_pri
	 WHERE hel.item = low_pri.item;

CREATE TABLE total_bandwidth AS
  SELECT sum(st.Mbs) FROM stores AS st, shopping_list AS sp
         WHERE sp.store = st.store;

