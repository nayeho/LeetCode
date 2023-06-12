# Write your MySQL query statement below

# id순서대로 정렬하여 행번호로 id 재부여
SELECT 
	ROW_NUMBER() OVER (ORDER BY u.id) as id
	, u.student as student

FROM (
# 짝수 > 홀수 (ex. 2번 > 1번)
SELECT 
	id-1 as id   # id-1을 해주어 id가 짝수인 것이 1 작은 홀수가 되도록
    , student
FROM seat
WHERE mod(id, 2) = 0   # 짝수만

UNION ALL

# 홀수 > 짝수 (ex. 1번 > 2번)
SELECT 
	id+1 as id   # id+1을 해주어 id가 홀수인 것이 1 큰 짝수가 되도록
	, student
FROM seat
WHERE mod(id, 2) = 1   # 홀수만
) u