# Write your MySQL query statement below

#SELF JOIN
WITH base_table AS(
    
    SELECT requester_id AS f1, accepter_id AS f2
    FROM RequestAccepted
    
    UNION
    
    SELECT accepter_id AS f1, requester_id AS f2
    FROM RequestAccepted
    
    ),
    base_table2 AS(
    SELECT f1 AS id, COUNT(f1) AS num, RANK() OVER(ORDER BY COUNT(f1) DESC) AS ranking
    FROM base_table
    GROUP BY f1
    )
    
SELECT id, num
FROM base_table2
WHERE ranking = 1

