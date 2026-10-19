-- 1174. Immediate Food Delivery II · Medium · https://leetcode.com/problems/immediate-food-delivery-ii/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Delivery (delivery_id int, customer_id int, order_date date, customer_pref_delivery_date date)
-- case: {"headers": {"Delivery": ["delivery_id", "customer_id", "order_date", "customer_pref_delivery_date"]}, "rows": {"Delivery": [[1, 1, "2019-08-01", "2019-08-02"], [2, 2, "2019-08-02", "2019-08-02"], [3, 1, "2019-08-11", "2019-08-12"], [4, 3, "2019-08-24", "2019-08-24"], [5, 3, "2019-08-21", "2019-08-22"], [6, 2, "2019-08-11", "2019-08-13"], [7, 4, "2019-08-09", "2019-08-09"]]}}
-- expect: {"columns": ["immediate_percentage"], "rows": [[50.0]], "ordered": false}
