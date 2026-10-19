-- 1193. Monthly Transactions I · Medium · https://leetcode.com/problems/monthly-transactions-i/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Transactions (id int, country varchar(4), state enum('approved', 'declined'), amount int, trans_date date)
-- case: {"headers": {"Transactions": ["id", "country", "state", "amount", "trans_date"]}, "rows": {"Transactions": [[121, "US", "approved", 1000, "2018-12-18"], [122, "US", "declined", 2000, "2018-12-19"], [123, "US", "approved", 2000, "2019-01-01"], [124, "DE", "approved", 2000, "2019-01-07"]]}}
-- expect: {"columns": ["month", "country", "trans_count", "approved_count", "trans_total_amount", "approved_total_amount"], "rows": [["2018-12", "US", 2, 1, 3000, 1000], ["2019-01", "US", 1, 1, 2000, 2000], ["2019-01", "DE", 1, 1, 2000, 2000]], "ordered": false}
