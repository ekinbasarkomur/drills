"""
1435. Create a Session Bar Chart · Easy · https://leetcode.com/problems/create-a-session-bar-chart/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def create_bar_chart(sessions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    sessions = frame(['session_id', 'duration'], [[1, 30], [2, 199], [3, 299], [4, 580], [5, 1000]], {'session_id': 'Int64', 'duration': 'Int64'})
    check(create_bar_chart(sessions), ['bin', 'total'], [['[0-5>', 3], ['[5-10>', 1], ['[10-15>', 0], ['15 or more', 1]], ordered=False)
