# Write your MySQL query statement below

WITH first_table AS
    (SELECT *,
    RANK() OVER(PARTITION BY product_id ORDER BY year ASC) AS ranking
    FROM sales
    )
    
SELECT product_id, year AS first_year, quantity, price
FROM first_table
WHERE ranking = 1

