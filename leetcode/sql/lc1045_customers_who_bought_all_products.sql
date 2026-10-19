-- 1045. Customers Who Bought All Products · Medium · https://leetcode.com/problems/customers-who-bought-all-products/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Customer (customer_id int, product_key int)
-- schema: Create table Product (product_key int)
-- case: {"headers": {"Customer": ["customer_id", "product_key"], "Product": ["product_key"]}, "rows": {"Customer": [[1, 5], [2, 6], [3, 5], [3, 6], [1, 6]], "Product": [[5], [6]]}}
-- expect: {"columns": ["customer_id"], "rows": [[1], [3]], "ordered": false}
