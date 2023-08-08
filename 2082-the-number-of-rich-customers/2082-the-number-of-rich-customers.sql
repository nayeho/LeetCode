# Write your MySQL query statement below

SELECT count(distinct(customer_id)) as rich_count
FROM Store
WHERE amount > 500
