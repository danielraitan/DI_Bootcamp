-- create table customer (
-- id serial primary key,
-- first_name varchar(20),
-- last_name varchar(20) ,
-- password varchar(10));

-- create table Customer_profile(
-- user_id int primary key,
-- isLoggedIn BOOLEAN DEFAULT FALSE ,
-- CONSTRAINT profile_user_id_fkey foreign key (user_id) references customer (id) on delete cascade); 

-- INSERT into customer(id, first_name, last_name, password)VALUES
-- (1, 'john', 'doe', 123),
-- (2,'jerome', 'lalu', 1234),
-- (3,'lea', 'rive', 12345);

-- INSERT into customer_profile(user_id,isloggedin)VALUES
-- (1, true),
-- (2, false);

-- select first_name, isloggedin from customer 
-- join customer_profile
-- on customer.id = customer_profile.user_id where isloggedin = 'true';

-- select first_name, isloggedin from customer_profile
-- right join customer
-- on customer.id = customer_profile.user_id;

-- select count(isloggedin) from customer_profile where isloggedin = 'false';

-- create table book(
-- book_id SERIAL PRIMARY KEY,
-- title TEXT NOT NULL,
-- author TEXT NOT NULL);

-- insert into book(book_id, title, author)VALUES
-- (1, 'Alice In Wonderland', 'Lewis Carroll'),
-- (2, 'Harry Potter', 'J.K Rowling'),
-- (3, 'To kill a mockingbird', 'Harper Lee');

-- create table Student(
-- student_id SERIAL PRIMARY KEY,
-- name text NOT NULL UNIQUE,
-- age int);

-- insert into student(student_id, name, age)VALUES
-- (1, 'John', 12),
-- (2, 'Lera', 11),
-- (3, 'Patrick', 10),
-- (4, 'Bob', 14);



