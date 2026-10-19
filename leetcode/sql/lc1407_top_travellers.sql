-- 1407. Top Travellers · Easy · https://leetcode.com/problems/top-travellers/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create Table If Not Exists Users (id int, name varchar(30))
-- schema: Create Table If Not Exists Rides (id int, user_id int, distance int)
-- case: {"headers": {"Users": ["id", "name"], "Rides": ["id", "user_id", "distance"]}, "rows": {"Users": [[1, "Alice"], [2, "Bob"], [3, "Alex"], [4, "Donald"], [7, "Lee"], [13, "Jonathan"], [19, "Elvis"]], "Rides": [[1, 1, 120], [2, 2, 317], [3, 3, 222], [4, 7, 100], [5, 13, 312], [6, 19, 50], [7, 7, 120], [8, 19, 400], [9, 7, 230]]}}
-- expect: {"columns": ["name", "travelled_distance"], "rows": [["Elvis", 450], ["Lee", 450], ["Bob", 317], ["Jonathan", 312], ["Alex", 222], ["Alice", 120], ["Donald", 0]], "ordered": true}
