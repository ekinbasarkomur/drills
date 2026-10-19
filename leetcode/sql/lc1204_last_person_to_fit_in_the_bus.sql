-- 1204. Last Person to Fit in the Bus · Medium · https://leetcode.com/problems/last-person-to-fit-in-the-bus/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Queue (person_id int, person_name varchar(30), weight int, turn int)
-- case: {"headers": {"Queue": ["person_id", "person_name", "weight", "turn"]}, "rows": {"Queue": [[5, "Alice", 250, 1], [4, "Bob", 175, 5], [3, "Alex", 350, 2], [6, "John Cena", 400, 3], [1, "Winston", 500, 6], [2, "Marie", 200, 4]]}}
-- expect: {"columns": ["person_name"], "rows": [["John Cena"]], "ordered": true}
