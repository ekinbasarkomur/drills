"""
1127. User Purchase Platform · Hard · https://leetcode.com/problems/user-purchase-platform/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def user_purchase(spending: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    spending = frame(['user_id', 'spend_date', 'platform', 'amount'], [[1, '2019-07-01', 'mobile', 100], [1, '2019-07-01', 'desktop', 100], [2, '2019-07-01', 'mobile', 100], [2, '2019-07-02', 'mobile', 100], [3, '2019-07-01', 'desktop', 100], [3, '2019-07-02', 'desktop', 100]], {'user_id': 'Int64', 'spend_date': 'datetime64[ns]', 'platform': 'object', 'amount': 'Int64'})
    check(user_purchase(spending), ['spend_date', 'platform', 'total_amount', 'total_users'], [['2019-07-01', 'desktop', 100, 1], ['2019-07-01', 'mobile', 100, 1], ['2019-07-01', 'both', 200, 1], ['2019-07-02', 'desktop', 100, 1], ['2019-07-02', 'mobile', 100, 1], ['2019-07-02', 'both', 0, 0]], ordered=False)
