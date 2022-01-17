#Keyi Jiang 20220116

#1. Median Employee Salary
#first solution
SELECT id, e.company, salary
FROM
    (SELECT id, company, salary, row_number() Over (Partition by company Order by salary) as sal_r
    FROM Employee) e
        JOIN
        (SELECT company, avg(sal_rank) as avg_sal
        FROM
            (SELECT company, row_number() Over (Partition by company Order by salary) as sal_rank
            FROM Employee) temp
        GROUP BY company )ae
    ON e.company = ae.company
    AND e.sal_r between floor(ae.avg_sal) and ceiling(ae.avg_sal)

#improved
SELECT id, company, salary
FROM
    (SELECT id, company, salary,
        row_number() Over (Partition by company Order by salary) as sal_rank,
        count(id) Over (Partition by company) as com_count
    FROM Employee)temp
WHERE sal_rank between com_count/2.0 and com_count/2.0+1


#2. Managers with at Least 5 Direct Reports
SELECT name
FROM Employee e
JOIN
    (SELECT managerId, count(id) as direct_reporters
    FROM Employee
    GROUP BY managerId
    HAVING direct_reporters >=5) e1
    ON e.id = e1.managerId

#3. Find Median Given Frequency of Numbers
SELECT round(avg(num),1) as median
FROM
    (SELECT num, frequency,
            sum(frequency) OVER (ORDER BY num) as cum_freq,
            (sum(frequency) OVER ())/2 as median_num
    FROM Numbers)n1
WHERE floor(median_num) between cum_freq-frequency and cum_freq
OR ceil(median_num) between cum_freq-frequency and cum_freq
