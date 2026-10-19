-- 1068. Product Sales Analysis I · Easy · https://leetcode.com/problems/product-sales-analysis-i/
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
-- schema: Create table If Not Exists Product (product_id int, product_name varchar(10))
-- case: {"headers": {"Sales": ["sale_id", "product_id", "year", "quantity", "price"], "Product": ["product_id", "product_name"]}, "rows": {"Sales": [[1, 100, 2008, 10, 5000], [2, 100, 2009, 12, 5000], [7, 200, 2011, 15, 9000]], "Product": [[100, "Nokia"], [200, "Apple"], [300, "Samsung"]]}}
-- expect: {"columns": ["product_name", "year", "price"], "rows": [["Nokia", 2008, 5000], ["Nokia", 2009, 5000], ["Apple", 2011, 9000]], "ordered": false}
