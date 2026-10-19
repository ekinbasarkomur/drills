-- 602. Friend Requests II: Who Has the Most Friends · Medium · https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists RequestAccepted (requester_id int not null, accepter_id int null, accept_date date null)
-- case: {"headers": {"RequestAccepted": ["requester_id", "accepter_id", "accept_date"]}, "rows": {"RequestAccepted": [[1, 2, "2016/06/03"], [1, 3, "2016/06/08"], [2, 3, "2016/06/08"], [3, 4, "2016/06/09"]]}}
-- expect: {"columns": ["id", "num"], "rows": [[3, 3]], "ordered": false}
