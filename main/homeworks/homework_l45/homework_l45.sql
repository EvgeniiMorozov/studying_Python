/*
 Для начала я попробывал объединить таблицы department и department_head
 по "логически общему" полю department.id
 */
SELECT dept.name AS department,
    dept_h.name AS head,
    dept.id AS id
FROM department dept
    JOIN department_head dept_h ON dept.id = dept_h.departmentid;
/*
 Финальный запрос будет следующим образом:
 Мы делаем выборку из двух таблиц (employee и полученной во вложенном запросе)
 по условию, id департаментов у нас равны в обоих таблицах.
 */
SELECT -- поля из таблицы employee
    emp.id AS id,
    emp.name AS Employee_name,
    -- поля из таблицы, полученной в подзапросе ниже
    dept.department AS Department,
    dept.head AS Head
FROM employee emp,
-- таблица - результат join`а таблиц department и depatment_head
    (
        SELECT dept.name AS department,
            dept_h.name AS head,
            dept.id AS id
        FROM department dept
        -- условие для объединения таблиц
            JOIN department_head dept_h ON dept.id = dept_h.departmentid
    ) dept
WHERE emp.departmentid = dept.id
GROUP BY id;
/*
 P.S. Илья, у меня не сработала группировка по полю id в результирующей таблице,
 не подскажешь, где я допустил ошибку.
 */