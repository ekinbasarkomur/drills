-- 1164. Product Price at a Given Date · Medium · https://leetcode.com/problems/product-price-at-a-given-date/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Products (product_id int, new_price int, change_date date)
-- case: {"headers": {"Products": ["product_id", "new_price", "change_date"]}, "rows": {"Products": [[1, 20, "2019-08-14"], [2, 50, "2019-08-14"], [1, 30, "2019-08-15"], [1, 35, "2019-08-16"], [2, 65, "2019-08-17"], [3, 20, "2019-08-18"]]}}
-- expect: {"columns": ["product_id", "price"], "rows": [[2, 50], [1, 35], [3, 10]], "ordered": false}
