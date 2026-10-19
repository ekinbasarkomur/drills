-- 1789. Primary Department for Each Employee · Easy · https://leetcode.com/problems/primary-department-for-each-employee/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Employee (employee_id int, department_id int, primary_flag ENUM('Y','N'))
-- case: {"headers": {"Employee": ["employee_id", "department_id", "primary_flag"]}, "rows": {"Employee": [["1", "1", "N"], ["2", "1", "Y"], ["2", "2", "N"], ["3", "3", "N"], ["4", "2", "N"], ["4", "3", "Y"], ["4", "4", "N"]]}}
-- expect: {"columns": ["employee_id", "department_id"], "rows": [[1, 1], [2, 1], [3, 3], [4, 3]], "ordered": false}
