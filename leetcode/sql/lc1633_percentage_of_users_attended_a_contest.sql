-- 1633. Percentage of Users Attended a Contest · Easy · https://leetcode.com/problems/percentage-of-users-attended-a-contest/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Users (user_id int, user_name varchar(20))
-- schema: Create table If Not Exists Register (contest_id int, user_id int)
-- case: {"headers": {"Users": ["user_id", "user_name"], "Register": ["contest_id", "user_id"]}, "rows": {"Users": [[6, "Alice"], [2, "Bob"], [7, "Alex"]], "Register": [[215, 6], [209, 2], [208, 2], [210, 6], [208, 6], [209, 7], [209, 6], [215, 7], [208, 7], [210, 2], [207, 2], [210, 7]]}}
-- expect: {"columns": ["contest_id", "percentage"], "rows": [[208, 100.0], [209, 100.0], [210, 100.0], [215, 66.67], [207, 33.33]], "ordered": true}
