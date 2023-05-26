# Write your MySQL query statement below

# SELECT DISTINCT(reports_to)
# FROM Employees
# WHERE reports_to IS NOT NULL

SELECT reports_to AS employee_id, (SELECT name FROM Employees s WHERE e.reports_to = s.employee_id) AS name, COUNT(reports_to) AS reports_count, ROUND(AVG(age), 0) AS average_age
FROM Employees e
WHERE reports_to IS NOT NULL
GROUP BY reports_to
ORDER BY employee_id
