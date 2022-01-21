#Keyi Jiang 20220120

#1. Count Student Number in Departments
SELECT dept_name, if(student_number is null, 0, student_number) as student_number
FROM Department d
    LEFT JOIN
    (SELECT dept_id, count(distinct student_id) as student_number
    FROM Student
    GROUP BY dept_id) s
    ON d.dept_id = s.dept_id
ORDER BY student_number DESC, dept_name ASC
