-- select first_name as first, last_name as last from employees;
-- SELECT DISTINCT department_id FROM employees;
-- select * from employees order by first_name desc;
-- select first_name, last_name, salary from employees;
-- select first_name, last_name, salary from employees order by salary ASC;
-- SELECT sum(salary) from employees;
-- SELECT max(salary), min(salary) from employees;
-- SELECT avg(salary) from employees;
-- select count(first_name) from employees;
-- select upper(first_name) from employees;
-- select left(first_name, 3) from employees;
-- select first_name|| ' ' ||last_name as full_name from employees;
-- select length(first_name|| ' ' ||last_name) as full_name from employees;
-- select first_name from employees where first_name ilike '%0|1|2|3|4|5|6|7|8|9%';
-- select first_name from employees where first_name ilike '%0|1|2|3|4|5|6|7|8|9%';
-- select first_name from employees limit 10;

-- select first_name, last_name, salary from employees where salary > 10000 and salary < 15000;
-- select first_name, last_name, hire_date from employees where hire_date > '1987-01-01' and hire_date < '1988-01-01';
-- select * from employees where first_name ilike '%c%e%';
-- select last_name, job_title, salary from employees 
-- join jobs
-- on jobs.job_id = employees.job_id
-- where job_title not like 'Programmers' and job_title not like 'Shipping Clerk' and salary != 4500 and salary != 10000 and salary != 15000;
-- select last_name from employees where last_name not like LEFT('last_name', 6);
--  select last_name from employees where last_name like '__e%';
-- select employees.*, job_title from employees 
-- join jobs
-- on jobs.job_id = employees.job_id;
-- select * from employees where last_name ilike 'JONES' and last_name ilike 'BLAKE' and last_name ilike 'SCOTT', and last_name ilike 'KING' and last_name ilike 'FORD';
