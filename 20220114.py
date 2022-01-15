#Keyi Jiang 20220114

#1. Delete Duplicate Emails
DELETE FROM Person WHERE id NOT IN
(SELECT id
FROM
    (SELECT id, email, row_number() OVER(PARTITION BY email ORDER BY id) as row_num
    FROM Person) p
WHERE row_num = 1)

#2. Rising Temperature
SELECT distinct w1.id
FROM Weather w1, Weather w2
WHERE w1.temperature > w2.temperature
AND DATEDIFF(w1.recordDate, w2.recordDate) = 1

#3. Trips and Users
SELECT t.request_at as Day, 
        round(count(if(status = 'completed', null, true))/count(id), 2) as 'Cancellation Rate'
FROM Trips t, Users u1, Users u2
    WHERE t.client_id = u1.users_id
    AND u1.banned = 'No'
    AND t.driver_id = u2.users_id
    AND u2.banned = 'No'
    AND request_at between '2013-10-01' and '2013-10-03'
GROUP BY request_at
ORDER BY request_At
