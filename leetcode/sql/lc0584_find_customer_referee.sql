-- 584. Find Customer Referee · Easy · https://leetcode.com/problems/find-customer-referee/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Customer (id int, name varchar(25), referee_id int)
-- case: {"headers": {"Customer": ["id", "name", "referee_id"]}, "rows": {"Customer": [[1, "Will", null], [2, "Jane", null], [3, "Alex", 2], [4, "Bill", null], [5, "Zack", 1], [6, "Mark", 2]]}}
-- expect: {"columns": ["name"], "rows": [["Will"], ["Jane"], ["Bill"], ["Zack"]], "ordered": false}
