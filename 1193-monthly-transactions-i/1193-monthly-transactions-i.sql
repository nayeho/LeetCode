# Write your MySQL query statement below

# SELECT LEFT(month, 7), country, trans_count, approved_count, trans_total_amount, approved_total_amount


SELECT LEFT(trans_date, 7) AS month,
        country,
        COUNT(LEFT(trans_date, 7)) AS trans_count,
        COUNT(CASE state WHEN 'approved' THEN 1 END) AS approved_count,
        SUM(amount) AS trans_total_amount,
        COALESCE(SUM(CASE state WHEN 'approved' THEN amount END), 0) AS approved_total_amount
FROM Transactions
GROUP BY LEFT(trans_date, 7), country

