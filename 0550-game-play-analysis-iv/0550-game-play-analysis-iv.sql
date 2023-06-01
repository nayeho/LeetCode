# Write your MySQL query statement below

# SELECT ROUND(COUNT(DISTINCT(a.player_id))
#     / (SELECT COUNT(DISTINCT(player_id)) FROM activity), 2) AS fraction
# FROM activity a
#     INNER JOIN activity i
#     ON a.player_id = i.player_id
#     AND a.device_id = i.device_id
# WHERE a.event_date = i.event_date - 1
    
# SELECT COUNT(DISTINCT(player_id) FROM activity

SELECT ROUND(COUNT(a2.player_id) / COUNT(a1.player_id),2) AS fraction
FROM (SELECT player_id, MIN(event_date) AS first_login FROM activity GROUP BY player_id) AS a1
LEFT JOIN Activity AS a2
ON a1.player_id = a2.player_id AND a1.first_login +1 = a2.event_date