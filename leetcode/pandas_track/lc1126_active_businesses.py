"""
1126. Active Businesses · Medium · https://leetcode.com/problems/active-businesses/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def active_businesses(events: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    events = frame(['business_id', 'event_type', 'occurrences'], [[1, 'reviews', 7], [3, 'reviews', 3], [1, 'ads', 11], [2, 'ads', 7], [3, 'ads', 6], [1, 'page views', 3], [2, 'page views', 12]], {'business_id': 'Int64', 'event_type': 'object', 'occurrences': 'Int64'})
    check(active_businesses(events), ['business_id'], [[1]], ordered=False)
