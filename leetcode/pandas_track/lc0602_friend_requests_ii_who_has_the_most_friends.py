"""
602. Friend Requests II: Who Has the Most Friends · Medium · https://leetcode.com/problems/friend-requests-ii-who-has-the-most-friends/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    request_accepted = frame(['requester_id', 'accepter_id', 'accept_date'], [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09']], {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    check(most_friends(request_accepted), ['id', 'num'], [[3, 3]], ordered=False)
