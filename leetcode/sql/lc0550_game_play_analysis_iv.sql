-- 550. Game Play Analysis IV · Medium · https://leetcode.com/problems/game-play-analysis-iv/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Activity (player_id int, device_id int, event_date date, games_played int)
-- case: {"headers": {"Activity": ["player_id", "device_id", "event_date", "games_played"]}, "rows": {"Activity": [[1, 2, "2016-03-01", 5], [1, 2, "2016-03-02", 6], [2, 3, "2017-06-25", 1], [3, 1, "2016-03-02", 0], [3, 4, "2018-07-03", 5]]}}
-- expect: {"columns": ["fraction"], "rows": [[0.33]], "ordered": false}
