#Keyi Jiang 20220111
#1. Combine Two Tables
SELECT firstName, lastName, city, state
FROM Person AS p
LEFT JOIN
Address AS a
ON p.personId = a.personId

#2. Second Highest Salary
#Accepted
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee)

#my way - cannot resolve null issue
SELECT salary as SecondHighestSalary
FROM
(SELECT salary, ROW_NUMBER() OVER (ORDER BY salary DESC) as row_num
FROM Employee AS e) t1
WHERE row_num = 2

#limit 1 offset 1; offset means remove the top 1

#3. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT * FROM
      (SELECT DISTINCT salary
      FROM
        (SELECT salary, dense_rank() OVER (ORDER BY salary DESC) as salary_rank
         FROM Employee)a
      WHERE salary_rank = N) temp
  );
END
