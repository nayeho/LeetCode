# Write your MySQL query statement below

WITH first_table AS(
    SELECT *,
    RANK() OVER(PARTITION BY customer_id ORDER BY order_date) AS ranking
    FROM delivery
    )
    
SELECT ROUND(AVG(CASE WHEN order_date = customer_pref_delivery_date THEN 1.00 ELSE 0.00 END) * 100, 2) AS immediate_percentage
FROM first_table
WHERE ranking = 1
