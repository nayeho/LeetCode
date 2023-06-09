# Write your MySQL query statement below

SELECT p.product_name, SUM(o.unit) AS unit
FROM Orders o
    INNER JOIN Products p
    ON o.product_id = p.product_id
WHERE order_date LIKE '2020-02%'
GROUP BY p.product_id
HAVING SUM(o.unit) >= 100