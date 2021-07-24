SELECT department, SUM(salary) as department_salary
FROM shop.employee
GROUP BY department
order by department_salary desc;

SELECT department, AVG(age) as department_age
FROM shop.employee
GROUP BY department
order by department_age desc;

SELECT department, age, AVG(salary) as department_salary
FROM shop.employee
GROUP BY department, age;

SELECT department, AVG(salary), SUM(salary) as department_salary
FROM shop.employee
GROUP BY department;

SELECT department, AVG(salary), SUM(salary), COUNT(salary)
FROM shop.employee
GROUP BY department;

SELECT department, AVG(salary), SUM(salary), COUNT(salary) as num_emp
FROM shop.employee
GROUP BY department
HAVING num_emp > 2;

select *
from employee
where id IN (
	select id
    from employee
    where salary > 2000
);

select *
from employee
where name IN (
	select name
    from customer
);

select *
from employee emp, (
	select * from customer
) cust
where emp.id = cust.id;

select *
from employee
where exists (
	select id
    from customer
    where id = 1
);
