#Keyi Jiang 20220115

#1. Game Play Analysis I
SELECT player_id, min(event_date) as first_login
FROM Activity
GROUP BY player_id

#2. Game Play Analysis II
SELECT a1.player_id, a2.device_id
FROM
    (SELECT player_id, min(event_date) as first_login
    FROM Activity
    GROUP BY player_id)a1
    LEFT JOIN Activity a2
    ON a1.player_id = a2.player_id
    AND a1.first_login = a2.event_date

#3. Game Play Analysis III
SELECT player_id, event_date,
        sum(games_played) OVER (
            Partition by player_id Order by event_date) as games_played_so_far
FROM Activity a
ORDER BY player_id, event_date

#4. Game Play Analysis IV
SELECT round(count(distinct a1.player_id)/count(distinct a.player_id),2) as fraction
FROM Activity a
LEFT JOIN
(SELECT player_id, min(event_date) as first_login
FROM Activity
GROUP BY player_id)a1
ON a.player_id = a1.player_id
AND datediff(a.event_date, a1.first_login) = 1
