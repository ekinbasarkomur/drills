-- 577. Employee Bonus · Easy · https://leetcode.com/problems/employee-bonus/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int)
-- schema: Create table If Not Exists Bonus (empId int, bonus int)
-- case: {"headers": {"Employee": ["empId", "name", "supervisor", "salary"], "Bonus": ["empId", "bonus"]}, "rows": {"Employee": [[3, "Brad", null, 4000], [1, "John", 3, 1000], [2, "Dan", 3, 2000], [4, "Thomas", 3, 4000]], "Bonus": [[2, 500], [4, 2000]]}}
-- expect: {"columns": ["name", "bonus"], "rows": [["Brad", null], ["John", null], ["Dan", 500]], "ordered": false}
