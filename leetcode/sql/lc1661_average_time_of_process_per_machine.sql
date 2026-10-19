-- 1661. Average Time of Process per Machine · Easy · https://leetcode.com/problems/average-time-of-process-per-machine/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Activity (machine_id int, process_id int, activity_type ENUM('start', 'end'), timestamp float)
-- case: {"headers": {"Activity": ["machine_id", "process_id", "activity_type", "timestamp"]}, "rows": {"Activity": [[0, 0, "start", 0.712], [0, 0, "end", 1.52], [0, 1, "start", 3.14], [0, 1, "end", 4.12], [1, 0, "start", 0.55], [1, 0, "end", 1.55], [1, 1, "start", 0.43], [1, 1, "end", 1.42], [2, 0, "start", 4.1], [2, 0, "end", 4.512], [2, 1, "start", 2.5], [2, 1, "end", 5]]}}
-- expect: {"columns": ["machine_id", "processing_time"], "rows": [[0, 0.894], [1, 0.995], [2, 1.456]], "ordered": false}
