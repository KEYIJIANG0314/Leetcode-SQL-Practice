-- * inner join

SELECT s.name
FROM SalesPerson s
WHERE s.sales_id NOT IN (SELECT sales_id 
                         FROM Orders o
                         INNER JOIN Company c
                         ON o.com_id = c.com_id
                         AND c.name = 'RED')