-- 620. Not Boring Movies · Easy · https://leetcode.com/problems/not-boring-movies/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists cinema (id int, movie varchar(255), description varchar(255), rating float(2, 1))
-- case: {"headers": {"cinema": ["id", "movie", "description", "rating"]}, "rows": {"cinema": [[1, "War", "great 3D", 8.9], [2, "Science", "fiction", 8.5], [3, "irish", "boring", 6.2], [4, "Ice song", "Fantacy", 8.6], [5, "House card", "Interesting", 9.1]]}}
-- expect: {"columns": ["id", "movie", "description", "rating"], "rows": [[5, "House card", "Interesting", 9.1], [1, "War", "great 3D", 8.9]], "ordered": true}
