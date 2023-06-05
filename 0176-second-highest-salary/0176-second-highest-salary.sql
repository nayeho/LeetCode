# Write your MySQL query statement below

WITH rank_table AS (
    SELECT id, salary, DENSE_RANK() OVER(ORDER BY salary DESC) AS ranking
    FROM employee
    )
  
# SELECT *
# FROM rank_table
  
SELECT (CASE WHEN count(id) = 0 THEN NULL ELSE salary END)AS SecondHighestSalary
FROM rank_table
WHERE ranking = 2
