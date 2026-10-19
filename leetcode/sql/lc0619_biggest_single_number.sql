-- 619. Biggest Single Number · Easy · https://leetcode.com/problems/biggest-single-number/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists MyNumbers (num int)
-- case: {"headers": {"MyNumbers": ["num"]}, "rows": {"MyNumbers": [[8], [8], [3], [3], [1], [4], [5], [6]]}}
-- expect: {"columns": ["num"], "rows": [[6]], "ordered": false}
-- case: {"headers": {"MyNumbers": ["num"]}, "rows": {"MyNumbers": [[8], [8], [7], [7], [3], [3], [3]]}}
-- expect: {"columns": ["num"], "rows": [[null]], "ordered": false}
