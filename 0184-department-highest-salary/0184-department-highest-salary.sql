# Write your MySQL query statement below

SELECT d.name AS Department
    , e.name AS Employee
    , e.salary AS Salary
FROM employee e
    INNER JOIN (
        SELECT departmentid, MAX(salary) AS max_salary
        FROM employee
        GROUP BY departmentid
    )e2 ON e.departmentid = e2.departmentid AND e.salary = e2.max_salary
    INNER JOIN department d ON e.departmentid = d.id
