-- 1581. Customer Who Visited but Did Not Make Any Transactions · Easy · https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Visits(visit_id int, customer_id int)
-- schema: Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int)
-- case: {"headers": {"Visits": ["visit_id", "customer_id"], "Transactions": ["transaction_id", "visit_id", "amount"]}, "rows": {"Visits": [[1, 23], [2, 9], [4, 30], [5, 54], [6, 96], [7, 54], [8, 54]], "Transactions": [[2, 5, 310], [3, 5, 300], [9, 5, 200], [12, 1, 910], [13, 2, 970]]}}
-- expect: {"columns": ["customer_id", "count_no_trans"], "rows": [[54, 2], [30, 1], [96, 1]], "ordered": false}
