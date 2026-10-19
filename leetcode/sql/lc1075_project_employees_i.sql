-- 1075. Project Employees I · Easy · https://leetcode.com/problems/project-employees-i/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Project (project_id int, employee_id int)
-- schema: Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int)
-- case: {"headers": {"Project": ["project_id", "employee_id"], "Employee": ["employee_id", "name", "experience_years"]}, "rows": {"Project": [[1, 1], [1, 2], [1, 3], [2, 1], [2, 4]], "Employee": [[1, "Khaled", 3], [2, "Ali", 2], [3, "John", 1], [4, "Doe", 2]]}}
-- expect: {"columns": ["project_id", "average_years"], "rows": [[1, 2.0], [2, 2.5]], "ordered": false}
