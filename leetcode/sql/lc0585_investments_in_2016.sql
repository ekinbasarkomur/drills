-- 585. Investments in 2016 · Medium · https://leetcode.com/problems/investments-in-2016/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create Table If Not Exists Insurance (pid int, tiv_2015 float, tiv_2016 float, lat float, lon float)
-- case: {"headers": {"Insurance": ["pid", "tiv_2015", "tiv_2016", "lat", "lon"]}, "rows": {"Insurance": [[1, 10, 5, 10, 10], [2, 20, 20, 20, 20], [3, 10, 30, 20, 20], [4, 10, 40, 40, 40]]}}
-- expect: {"columns": ["tiv_2016"], "rows": [[45.0]], "ordered": false}
