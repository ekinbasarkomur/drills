-- 1729. Find Followers Count · Easy · https://leetcode.com/problems/find-followers-count/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Followers(user_id int, follower_id int)
-- case: {"headers": {"Followers": ["user_id", "follower_id"]}, "rows": {"Followers": [["0", "1"], ["1", "0"], ["2", "0"], ["2", "1"]]}}
-- expect: {"columns": ["user_id", "followers_count"], "rows": [[0, 1], [1, 1], [2, 2]], "ordered": true}
