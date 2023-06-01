# Write your MySQL query statement below

SELECT DISTINCT l.num AS consecutiveNums  -- Num 이 고유값으로 나타나게 
FROM(
    SELECT id, num
        , LAG(num) OVER (ORDER BY id) AS 'lag'   -- Num - 1
        , LEAD(num) OVER (ORDER By id) AS 'lead'   -- Num + 1
    FROM logs) l
WHERE l.num = l.lag AND l.num = l.lead
