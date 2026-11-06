"""
1699. Number of Calls Between Two Persons · Medium · https://leetcode.com/problems/number-of-calls-between-two-persons/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def number_of_calls(calls: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    calls = frame(['from_id', 'to_id', 'duration'], [[1, 2, 59], [2, 1, 11], [1, 3, 20], [3, 4, 100], [3, 4, 200], [3, 4, 200], [4, 3, 499]], {'from_id': 'Int64', 'to_id': 'Int64', 'duration': 'Int64'})
    check(number_of_calls(calls), ['person1', 'person2', 'call_count', 'total_duration'], [[1, 2, 2, 70], [1, 3, 1, 20], [3, 4, 4, 999]], ordered=False)
