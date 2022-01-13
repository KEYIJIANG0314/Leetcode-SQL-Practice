#Keyi Jiang 20220113

#1. Customers Who Never Order
Select name as Customers
FROM
    (Customers as c
    LEFT JOIN
    Orders as o
    ON c.id = o.customerID)
WHERE customerId is null

#2. Department Highest Salary
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM
    (SELECT departmentId, name, salary,
            rank() OVER (Partition by departmentId Order by salary DESC) as rank_sal
    FROM Employee) as e
    LEFT JOIN
    Department as d
    ON e.departmentId = d.id
WHERE e.rank_sal = 1

#3. Department Top Three Salaries
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM
    (SELECT departmentId, name, salary,
            dense_rank() OVER (Partition by departmentId Order by salary DESC) as rank_sal
    FROM Employee) as e
    LEFT JOIN
    Department as d
    ON e.departmentId = d.id
WHERE e.rank_sal <= 3

#same answer
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM
    (SELECT departmentId, name, salary,
            dense_rank() OVER (Partition by departmentId Order by salary DESC) as rank_sal
    FROM Employee) as e
    JOIN
    Department as d
    ON e.departmentId = d.id
    AND e.rank_sal <= 3
