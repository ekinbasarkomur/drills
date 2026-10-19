-- 1251. Average Selling Price · Easy · https://leetcode.com/problems/average-selling-price/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int)
-- schema: Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int)
-- case: {"headers": {"Prices": ["product_id", "start_date", "end_date", "price"], "UnitsSold": ["product_id", "purchase_date", "units"]}, "rows": {"Prices": [[1, "2019-02-17", "2019-02-28", 5], [1, "2019-03-01", "2019-03-22", 20], [2, "2019-02-01", "2019-02-20", 15], [2, "2019-02-21", "2019-03-31", 30]], "UnitsSold": [[1, "2019-02-25", 100], [1, "2019-03-01", 15], [2, "2019-02-10", 200], [2, "2019-03-22", 30]]}}
-- expect: {"columns": ["product_id", "average_price"], "rows": [[1, 6.96], [2, 16.96]], "ordered": false}
