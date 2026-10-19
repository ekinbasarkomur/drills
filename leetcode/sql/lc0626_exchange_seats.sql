-- 626. Exchange Seats · Medium · https://leetcode.com/problems/exchange-seats/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Seat (id int, student varchar(255))
-- case: {"headers": {"Seat": ["id", "student"]}, "rows": {"Seat": [[1, "Abbot"], [2, "Doris"], [3, "Emerson"], [4, "Green"], [5, "Jeames"]]}}
-- expect: {"columns": ["id", "student"], "rows": [[1, "Doris"], [2, "Abbot"], [3, "Green"], [4, "Emerson"], [5, "Jeames"]], "ordered": true}
