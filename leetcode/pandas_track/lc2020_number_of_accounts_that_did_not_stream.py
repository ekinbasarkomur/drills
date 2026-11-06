"""
2020. Number of Accounts That Did Not Stream · Medium · https://leetcode.com/problems/number-of-accounts-that-did-not-stream/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_target_accounts(subscriptions: pd.DataFrame, streams: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    subscriptions = frame(['account_id', 'start_date', 'end_date'], [[9, '2020-02-18', '2021-10-30'], [3, '2021-09-21', '2021-11-13'], [11, '2020-02-28', '2020-08-18'], [13, '2021-04-20', '2021-09-22'], [4, '2020-10-26', '2021-05-08'], [5, '2020-09-11', '2021-01-17']], {'account_id': 'Int64', 'start_date': 'datetime64[ns]', 'end_date': 'datetime64[ns]'})
    streams = frame(['session_id', 'account_id', 'stream_date'], [[14, 9, '2020-05-16'], [16, 3, '2021-10-27'], [18, 11, '2020-04-29'], [17, 13, '2021-08-08'], [19, 4, '2020-12-31'], [13, 5, '2021-01-05']], {'session_id': 'Int64', 'account_id': 'Int64', 'stream_date': 'datetime64[ns]'})
    check(find_target_accounts(subscriptions, streams), ['accounts_count'], [[2]], ordered=False)
