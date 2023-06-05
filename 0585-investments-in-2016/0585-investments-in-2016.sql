# Write your MySQL query statement below


# WITH base_table AS(
#     SELECT i1.pid AS id
#     FROM insurance i1, insurance i2
#     WHERE i1.lat = i2.lat
#     AND i1.lon = i2.lon
#     AND i1.pid != i2.pid
#     AND i1.tiv_2015 != i2.tiv_2015
#     )
    
# SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
# FROM insurance
# WHERE pid NOT IN(SELECT id
#                 FROM base_table)

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016 
FROM insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM insurance 
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
    )
AND CONCAT(lat, lon) IN (
    SELECT CONCAT(lat, lon)
    FROM insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
    )
