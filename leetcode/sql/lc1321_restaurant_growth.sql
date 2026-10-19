-- 1321. Restaurant Growth · Medium · https://leetcode.com/problems/restaurant-growth/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Customer (customer_id int, name varchar(20), visited_on date, amount int)
-- case: {"headers": {"Customer": ["customer_id", "name", "visited_on", "amount"]}, "rows": {"Customer": [[1, "Jhon", "2019-01-01", 100], [2, "Daniel", "2019-01-02", 110], [3, "Jade", "2019-01-03", 120], [4, "Khaled", "2019-01-04", 130], [5, "Winston", "2019-01-05", 110], [6, "Elvis", "2019-01-06", 140], [7, "Anna", "2019-01-07", 150], [8, "Maria", "2019-01-08", 80], [9, "Jaze", "2019-01-09", 110], [1, "Jhon", "2019-01-10", 130], [3, "Jade", "2019-01-10", 150]]}}
-- expect: {"columns": ["visited_on", "amount", "average_amount"], "rows": [["2019-01-07", 860, 122.86], ["2019-01-08", 840, 120], ["2019-01-09", 840, 120], ["2019-01-10", 1000, 142.86]], "ordered": true}
