#Keyi Jiang 20220112
#1. Rank Scores
SELECT score,
        DENSE_RANK() OVER (ORDER BY score DESC) as 'rank'
FROM Scores
ORDER BY score DESC

#2. Consecutive Numbers
SELECT distinct num as ConsecutiveNums
FROM
    (SELECT num,
    lag(num) over (order by id) as before_val,
    lead(num) over (order by id) as after_val
    FROM logs) temp
WHERE num = before_val
and before_val = after_val

#first answer to be improved solution
SELECT num as ConsecutiveNums
FROM
    (SELECT DISTINCT num,
           first_value(id) OVER(Partition by num ORDER BY id) as first_val,
           last_value(id) Over (Partition by num ORDER BY id
                 rows Between current row and 2 following) as last_val
    FROM Logs)temp
WHERE (last_val - first_val) = 2

#3. Employees Earning More Than Their Managers
SELECT e1.name as Employee
FROM
(Employee as e1
JOIN
Employee as e2
ON e1.managerId = e2.id
AND e1.salary > e2.salary)

#4. Duplicate Emails
SELECT Email
    FROM person
    GROUP BY Email
    HAVING COUNT(Email) > 1
