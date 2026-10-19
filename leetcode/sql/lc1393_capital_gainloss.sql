-- 1393. Capital Gain/Loss · Medium · https://leetcode.com/problems/capital-gainloss/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create Table If Not Exists Stocks (stock_name varchar(15), operation ENUM('Sell', 'Buy'), operation_day int, price int)
-- case: {"headers": {"Stocks": ["stock_name", "operation", "operation_day", "price"]}, "rows": {"Stocks": [["Leetcode", "Buy", 1, 1000], ["Corona Masks", "Buy", 2, 10], ["Leetcode", "Sell", 5, 9000], ["Handbags", "Buy", 17, 30000], ["Corona Masks", "Sell", 3, 1010], ["Corona Masks", "Buy", 4, 1000], ["Corona Masks", "Sell", 5, 500], ["Corona Masks", "Buy", 6, 1000], ["Handbags", "Sell", 29, 7000], ["Corona Masks", "Sell", 10, 10000]]}}
-- expect: {"columns": ["stock_name", "capital_gain_loss"], "rows": [["Corona Masks", 9500], ["Leetcode", 8000], ["Handbags", -23000]], "ordered": false}
