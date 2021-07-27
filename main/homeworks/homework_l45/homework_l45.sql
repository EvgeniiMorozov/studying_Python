/*
Для начала я попробывал объединить таблицы department и department_head
по общему логическому полю department.id
*/

SELECT dept.name AS department,
    dept_h.name AS head
FROM department dept
    LEFT JOIN department_head dept_h ON dept.id = dept_h.departmentid;


