# Write your MySQL query statement below

WITH base_table AS (
    SELECT *,
    RANK() OVER(PARTITION BY product_id ORDER BY change_date DESC) AS ranking
    FROM products
    WHERE change_date <= '2019-08-16'
    )

SELECT p.product_id, COALESCE(new_price, 10) AS price
FROM (SELECT DISTINCT(product_id) FROM products) p
    LEFT JOIN (SELECT * FROM base_table WHERE ranking = 1) b
    ON p.product_id = b.product_id


