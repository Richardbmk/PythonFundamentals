>> CREATE TABLE dogs (
    name TEXT,
    breed TEXT,
    age INTEGER
);

>> CREATE TABLE cats (name TEXT, breed TEXT, age INTEGER);

>> .open dogs_db.db -- To create a data base, sqlite3 doenst save
--- data base you have to crear a data base
-- to store de data.

>> sqlite3 cats_db.db
>> CREATE TABLE cats (name TEXT, breed TEXT, age INTEGER);
>> .exit
>> sqlite3 cats_db.db
>> .tables
>> INSERT INTO cats (name, breed, age) VALUES ("Blue", "Scottish Fold", 3);
>> SELECT * FROM cats;
>> INSERT INTO cats (name, breed, age) VALUES ("Charlie", 35, "Tabby");
>> SELECT * FROM cats;

--- INSERT DATA FROM A FILE
>> .read basic.sql
>> .tables
>> SELECT * FROM dogs;

--- 360. SQL Basics: Selecting
>> SELECT * FROM dogs;
>> SELECT name FROM dogs;
>> SELECT name, age FROM dogs;
>> SELECT * FROM dogs WHERE name IS "Piggy";
>> SELECT * FROM dogs WHERE breed IS "Husky";
>> SELECT name FROM dogs WHERE breed IS "Husky";
>> SELECT * FROM dogs WHERE breed IS NOT "Chihuahua";
>> SELECT * FROM dogs WHERE breed IS NOT "Chihuahua" AND breed IS NOT "Pug";
>> SELECT * FROM dogs WHERE age > 9;
>> SELECT * FROM dogs WHERE age > 8;
>> SELECT * FROM dogs WHERE name LIKE "%gg%";

--- 361. Connecting to a DB With Python
>> python friends_SQL.py
>> dir
>> sqlite3 my_friends.db
>> .tables
>> .schema friends

--- 367. Scraping to a Database Pt. 2
>> SELECT title FROM books WHERE rating >= 4;