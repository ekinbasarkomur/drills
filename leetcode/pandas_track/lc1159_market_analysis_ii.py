"""
1159. Market Analysis II · Hard · https://leetcode.com/problems/market-analysis-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'join_date', 'favorite_brand'], [[1, '2019-01-01', 'Lenovo'], [2, '2019-02-09', 'Samsung'], [3, '2019-01-19', 'LG'], [4, '2019-05-21', 'HP']], {'user_id': 'Int64', 'join_date': 'datetime64[ns]', 'favorite_brand': 'object'})
    orders = frame(['order_id', 'order_date', 'item_id', 'buyer_id', 'seller_id'], [[1, '2019-08-01', 4, 1, 2], [2, '2019-08-02', 2, 1, 3], [3, '2019-08-03', 3, 2, 3], [4, '2019-08-04', 1, 4, 2], [5, '2019-08-04', 1, 3, 4], [6, '2019-08-05', 2, 2, 4]], {'order_id': 'Int64', 'order_date': 'datetime64[ns]', 'item_id': 'Int64', 'buyer_id': 'Int64', 'seller_id': 'Int64'})
    items = frame(['item_id', 'item_brand'], [[1, 'Samsung'], [2, 'Lenovo'], [3, 'LG'], [4, 'HP']], {'item_id': 'Int64', 'item_brand': 'object'})
    check(market_analysis(users, orders, items), ['seller_id', '2nd_item_fav_brand'], [[1, 'no'], [2, 'yes'], [3, 'yes'], [4, 'no']], ordered=False)
