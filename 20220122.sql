 -- Keyi Jiang 20220122
 -- 1. Find Customer Referee
SELECT name
FROM Customer
WHERE referee_id != 2
OR referee_id IS NULL
 
 -- 2. Investments in 2016
SELECT round(sum(i1.tiv_2016),2) as tiv_2016
FROM Insurance i1
    Inner Join
    (SELECT pid, tiv_2016,
        count(pid) OVER(partition by tiv_2015) as tiv_2015_count,
        count(pid) OVER(partition by lat,lon) as lat_lon_count
    FROM Insurance) i2
    ON i1.pid = i2.pid
    AND i2.tiv_2015_count > 1
    AND i2.lat_lon_count = 1

 -- 3. Customer Placing the Largest Number of Orders
SELECT customer_number
FROM Orders
Group by customer_number
ORDER BY count(order_number) DESC
LIMIT 1

 -- 3 Improved
SELECT customer_number
FROM Orders
Group by customer_number
Having count(order_number) >= ALL (SELECT count(order_number) as order_numbers
                                    FROM Orders
                                    Group by customer_number)