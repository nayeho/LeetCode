# Write your MySQL query statement below

select name as results
from (

(select name,count(*) as num
from movierating left join users
on movierating.user_id = users.user_id
group by movierating.user_id
order by num desc, name limit 1 )

union

(select title,avg(rating) as rat
from movierating left join movies
on movierating.movie_id = movies.movie_id
where month(created_at) = 2 and year(created_at) = 2020
group by movierating.movie_id
order by rat desc,title limit 1)
) as a