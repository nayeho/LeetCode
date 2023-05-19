# Write your MySQL query statement below

# 이제 대문자로 키워드 사용하자

SELECT today.id
FROM Weather today INNER JOIN Weather yesterday 
ON date_add(yesterday.recordDate, INTERVAL 1 DAY) = today.recordDate
WHERE today.temperature > yesterday.temperature;
