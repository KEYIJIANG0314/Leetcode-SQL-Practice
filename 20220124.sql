 -- Keyi Jiang 20220124
 -- 1. Big Countries
SELECT name, population, area
FROM World
WHERE area >= 3000000
OR population >= 25000000
;

 -- 2. Classes More Than 5 Students
SELECT class
FROM courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5
;

 -- 3. Friend Requests I: Overall Acceptance Rate
SELECT round(ifnull(count(distinct requester_id, accepter_id) 
             / count(distinct sender_id, send_to_id),0.00), 2) as accept_rate
FROM RequestAccepted, FriendRequest;


 -- 4. 	Friend Requests II: Who Has the Most Friends
SELECT left_id as id, count(distinct right_id) as num
FROM
    (SELECT requester_id as left_id, accepter_id as right_id
    FROM RequestAccepted 
    UNION 
    SELECT accepter_id as left_id, requester_id as right_id
    FROM RequestAccepted)temp
GROUP BY left_id
ORDER BY num DESC
LIMIT 1
;