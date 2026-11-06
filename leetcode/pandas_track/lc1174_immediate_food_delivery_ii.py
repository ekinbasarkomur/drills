"""
1174. Immediate Food Delivery II · Medium · https://leetcode.com/problems/immediate-food-delivery-ii/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    delivery = frame(['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date'], [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-12'], [4, 3, '2019-08-24', '2019-08-24'], [5, 3, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13'], [7, 4, '2019-08-09', '2019-08-09']], {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_pref_delivery_date': 'datetime64[ns]'})
    check(immediate_food_delivery(delivery), ['immediate_percentage'], [[50.0]], ordered=False)
