-- 1978. Employees Whose Manager Left the Company · Easy · https://leetcode.com/problems/employees-whose-manager-left-the-company/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Employees (employee_id int, name varchar(20), manager_id int, salary int)
-- case: {"headers": {"Employees": ["employee_id", "name", "manager_id", "salary"]}, "rows": {"Employees": [[3, "Mila", 9, 60301], [12, "Antonella", null, 31000], [13, "Emery", null, 67084], [1, "Kalel", 11, 21241], [9, "Mikaela", null, 50937], [11, "Joziah", 6, 28485]]}}
-- expect: {"columns": ["employee_id"], "rows": [[11]], "ordered": true}
