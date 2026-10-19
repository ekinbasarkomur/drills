"""
1173. Immediate Food Delivery I · Easy · https://leetcode.com/problems/immediate-food-delivery-i/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    delivery = frame(['delivery_id', 'customer_id', 'order_date', 'customer_pref_delivery_date'], [[1, 1, '2019-08-01', '2019-08-02'], [2, 5, '2019-08-02', '2019-08-02'], [3, 1, '2019-08-11', '2019-08-11'], [4, 3, '2019-08-24', '2019-08-26'], [5, 4, '2019-08-21', '2019-08-22'], [6, 2, '2019-08-11', '2019-08-13']], {'delivery_id': 'Int64', 'customer_id': 'Int64', 'order_date': 'datetime64[ns]', 'customer_pref_delivery_date': 'datetime64[ns]'})
    food_delivery(delivery)
