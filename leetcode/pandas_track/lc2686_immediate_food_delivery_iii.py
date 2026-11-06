"""
2686. Immediate Food Delivery III · Medium · https://leetcode.com/problems/immediate-food-delivery-iii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def immediate_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    delivery = frame(['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date'], [[1, 1, '2019-08-01', '2019-08-02'], [2, 2, '2019-08-01', '2019-08-01'], [3, 1, '2019-08-01', '2019-08-01'], [4, 3, '2019-08-02', '2019-08-13'], [5, 3, '2019-08-02', '2019-08-02'], [6, 2, '2019-08-02', '2019-08-02'], [7, 4, '2019-08-03', '2019-08-03'], [8, 1, '2019-08-03', '2019-08-03'], [9, 5, '2019-08-04', '2019-08-18'], [10, 2, '2019-08-04', '2019-08-18']], {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_pref_delivery_date': 'datetime64[ns]'})
    check(immediate_delivery(delivery), ['order_date', 'immediate_percentage'], [['2019-08-01', 66.67], ['2019-08-02', 66.67], ['2019-08-03', 100.0], ['2019-08-04', 0.0]], ordered=True)
