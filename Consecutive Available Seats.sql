-- Method 1
SELECT seat_id
FROM Cinema c
WHERE free = 1
AND (c.seat_id+1 in (SELECT seat_id From Cinema WHERE free = 1)
     or 
     c.seat_id-1 in (SELECT seat_id From Cinema WHERE free = 1))
ORDER BY seat_id
;

-- Method 2 - Using lag and lead to speed up and save space from multiple select
SELECT seat_id
FROM
    (SELECT seat_id, free, 
            lag(free) OVER (ORDER BY seat_id) as previous_seat,
            lead(free) OVER (ORDER BY seat_id) as next_seat
    FROM Cinema)temp
WHERE free = 1
AND (previous_seat = 1
     or 
     next_seat = 1)
ORDER BY seat_id
;