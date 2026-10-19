-- 185. Department Top Three Salaries · Hard · https://leetcode.com/problems/department-top-three-salaries/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int)
-- schema: Create table If Not Exists Department (id int, name varchar(255))
-- case: {"headers": {"Employee": ["id", "name", "salary", "departmentId"], "Department": ["id", "name"]}, "rows": {"Employee": [[1, "Joe", 85000, 1], [2, "Henry", 80000, 2], [3, "Sam", 60000, 2], [4, "Max", 90000, 1], [5, "Janet", 69000, 1], [6, "Randy", 85000, 1], [7, "Will", 70000, 1]], "Department": [[1, "IT"], [2, "Sales"]]}}
-- expect: {"columns": ["Department", "Employee", "Salary"], "rows": [["IT", "Max", 90000], ["IT", "Joe", 85000], ["IT", "Randy", 85000], ["IT", "Will", 70000], ["Sales", "Henry", 80000], ["Sales", "Sam", 60000]], "ordered": false}
