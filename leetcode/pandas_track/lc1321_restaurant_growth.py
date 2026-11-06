"""
1321. Restaurant Growth · Medium · https://leetcode.com/problems/restaurant-growth/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customer = frame(['customer_id', 'name', 'visited_on', 'amount'], [[1, 'Jhon', '2019-01-01', 100], [2, 'Daniel', '2019-01-02', 110], [3, 'Jade', '2019-01-03', 120], [4, 'Khaled', '2019-01-04', 130], [5, 'Winston', '2019-01-05', 110], [6, 'Elvis', '2019-01-06', 140], [7, 'Anna', '2019-01-07', 150], [8, 'Maria', '2019-01-08', 80], [9, 'Jaze', '2019-01-09', 110], [1, 'Jhon', '2019-01-10', 130], [3, 'Jade', '2019-01-10', 150]], {'customer_id': 'Int64', 'name': 'object', 'visited_on': 'datetime64[ns]', 'amount': 'Int64'})
    check(restaurant_growth(customer), ['visited_on', 'amount', 'average_amount'], [['2019-01-07', 860, 122.86], ['2019-01-08', 840, 120], ['2019-01-09', 840, 120], ['2019-01-10', 1000, 142.86]], ordered=True)
