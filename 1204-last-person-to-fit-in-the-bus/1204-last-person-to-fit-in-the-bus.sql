# Write your MySQL query statement below

WITH base_table AS (
    SELECT *,
    RANK() OVER(ORDER BY running_total DESC) AS ranking
    FROM(
        SELECT *,
        SUM(weight) OVER(ORDER BY turn) AS running_total
        FROM queue) q
        WHERE running_total <= 1000
        )
        
SELECT person_name
FROM base_table
WHERE ranking = 1
