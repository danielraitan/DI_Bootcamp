-- UPDATE language
-- SET name = 'Chinese ' WHERE language_id = 2;
-- select * from language;
-- select * from customer_review;
-- DROP TABLE customer_review;
-- SELECT * from actor where last_name ilike 'Monroe';
-- select * from film_actor where actor_id = 120;
-- select film.film_id, title, description, actor_id from film 
-- join film_actor
-- on film.film_id = film_actor.film_id 
-- WHERE actor_id = 120 and description ilike '%sumo%';
-- select * from film where length < 60 and rating = 'R' ;
-- select * from film where rental_rate > 4.0 and last_update >='2005-07-28' and last_update <='2005-08-01';
-- SELECT title, description, replacement_cost from film WHERE description ilike '%boat%' and replacement_cost=(select max(replacement_cost) from film);


