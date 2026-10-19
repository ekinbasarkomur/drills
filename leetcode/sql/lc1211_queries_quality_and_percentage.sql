-- 1211. Queries Quality and Percentage · Easy · https://leetcode.com/problems/queries-quality-and-percentage/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Queries (query_name varchar(30), result varchar(50), position int, rating int)
-- case: {"headers": {"Queries": ["query_name", "result", "position", "rating"]}, "rows": {"Queries": [["Dog", "Golden Retriever", 1, 5], ["Dog", "German Shepherd", 2, 5], ["Dog", "Mule", 200, 1], ["Cat", "Shirazi", 5, 2], ["Cat", "Siamese", 3, 3], ["Cat", "Sphynx", 7, 4]]}}
-- expect: {"columns": ["query_name", "quality", "poor_query_percentage"], "rows": [["Dog", 2.5, 33.33], ["Cat", 0.66, 33.33]], "ordered": false}
