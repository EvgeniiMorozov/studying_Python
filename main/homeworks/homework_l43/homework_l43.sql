SELECT department,
    MAX(salary) AS max_salary,
    AVG(salary) AS average_salary,
    MIN(salary) AS min_salary
FROM `shop`.`employee`
GROUP BY department;