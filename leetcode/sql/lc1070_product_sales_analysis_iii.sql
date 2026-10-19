-- 1070. Product Sales Analysis III · Medium · https://leetcode.com/problems/product-sales-analysis-iii/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int)
-- case: {"headers": {"Sales": ["sale_id", "product_id", "year", "quantity", "price"]}, "rows": {"Sales": [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]]}}
-- expect: {"columns": ["product_id", "first_year", "quantity", "price"], "rows": [[100, 2008, 10, 5000], [200, 2011, 15, 9000]], "ordered": false}
