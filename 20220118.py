#Keyi Jiang 20220118

#1. Winning Candidate
SELECT name
FROM Candidate c
    JOIN
    (SELECT candidateId, count(candidateId) as vote_times
    FROM vote
    GROUP BY candidateId) v
    ON c.id = v.candidateId
ORDER BY vote_times DESC
LIMIT 1

#2. Employee Bonus
SELECT name, bonus
FROM Employee e
    LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE (b.bonus < 1000 or b.bonus is null)

#3. Get Highest Answer Rate Question
SELECT question_id as survey_log
FROM
    (SELECT distinct question_id,
        count(if(action = 'show', 1, NULL)) as showed_times,
        count(if(action = 'answer', 1, NULL)) as answered_times
    FROM SurveyLog
    GROUP BY question_id)temp
ORDER BY answered_times/showed_times DESC, question_id
LIMIT 1
