-- 1731. The Number of Employees Which Report to Each Employee · Easy · https://leetcode.com/problems/the-number-of-employees-which-report-to-each-employee/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Employees(employee_id int, name varchar(20), reports_to int, age int)
-- case: {"headers": {"Employees": ["employee_id", "name", "reports_to", "age"]}, "rows": {"Employees": [[9, "Hercy", null, 43], [6, "Alice", 9, 41], [4, "Bob", 9, 36], [2, "Winston", null, 37]]}}
-- expect: {"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [[9, "Hercy", 2, 39]], "ordered": true}
-- case: {"headers": {"Employees": ["employee_id", "name", "reports_to", "age"]}, "rows": {"Employees": [[1, "Michael", null, 45], [2, "Alice", 1, 38], [3, "Bob", 1, 42], [4, "Charlie", 2, 34], [5, "David", 2, 40], [6, "Eve", 3, 37], [7, "Frank", null, 50], [8, "Grace", null, 48]]}}
-- expect: {"columns": ["employee_id", "name", "reports_count", "average_age"], "rows": [["-----------", "-------", "-------------", "-----------"], [1, "Michael", 2, 40], [2, "Alice", 2, 37], [3, "Bob", 1, 37]], "ordered": true}
