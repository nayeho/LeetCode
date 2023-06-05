# Write your MySQL query statement below

# SELF JOIN

SELECT a.visited_on, SUM(b.amount) AS amount, ROUND(SUM(b.amount)/7, 2) AS average_amount
FROM (SELECT visited_on, SUM(amount) AS amount
      FROM customer
      GROUP BY visited_on
     ) a,
     (SELECT visited_on, SUM(amount) AS amount
      FROM customer GROUP BY visited_on
     ) b
WHERE DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6
GROUP BY a.visited_on
HAVING COUNT(DISTINCT b.visited_on) = 7