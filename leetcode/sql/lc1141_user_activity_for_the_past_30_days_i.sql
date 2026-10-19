-- 1141. User Activity for the Past 30 Days I · Easy · https://leetcode.com/problems/user-activity-for-the-past-30-days-i/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Activity (user_id int, session_id int, activity_date date, activity_type ENUM('open_session', 'end_session', 'scroll_down', 'send_message'))
-- case: {"headers": {"Activity": ["user_id", "session_id", "activity_date", "activity_type"]}, "rows": {"Activity": [[1, 1, "2019-07-20", "open_session"], [1, 1, "2019-07-20", "scroll_down"], [1, 1, "2019-07-20", "end_session"], [2, 4, "2019-07-20", "open_session"], [2, 4, "2019-07-21", "send_message"], [2, 4, "2019-07-21", "end_session"], [3, 2, "2019-07-21", "open_session"], [3, 2, "2019-07-21", "send_message"], [3, 2, "2019-07-21", "end_session"], [4, 3, "2019-06-25", "open_session"], [4, 3, "2019-06-25", "end_session"]]}}
-- expect: {"columns": ["day", "active_users"], "rows": [["2019-07-20", 2], ["2019-07-21", 2]], "ordered": false}
