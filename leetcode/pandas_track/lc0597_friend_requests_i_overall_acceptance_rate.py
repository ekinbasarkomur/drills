"""
597. Friend Requests I: Overall Acceptance Rate · Easy · https://leetcode.com/problems/friend-requests-i-overall-acceptance-rate/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def acceptance_rate(friend_request: pd.DataFrame, request_accepted: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    friend_request = frame(['sender_id', 'send_to_id', 'request_date'], [[1, 2, '2016/06/01'], [1, 3, '2016/06/01'], [1, 4, '2016/06/01'], [2, 3, '2016/06/02'], [3, 4, '2016/06/09']], {'sender_id': 'Int64', 'send_to_id': 'Int64', 'request_date': 'datetime64[ns]'})
    request_accepted = frame(['requester_id', 'accepter_id', 'accept_date'], [[1, 2, '2016/06/03'], [1, 3, '2016/06/08'], [2, 3, '2016/06/08'], [3, 4, '2016/06/09'], [3, 4, '2016/06/10']], {'requester_id': 'Int64', 'accepter_id': 'Int64', 'accept_date': 'datetime64[ns]'})
    check(acceptance_rate(friend_request, request_accepted), ['accept_rate'], [[0.8]], ordered=False)
