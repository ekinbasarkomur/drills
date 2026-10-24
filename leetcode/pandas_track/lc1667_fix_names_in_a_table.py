"""
1667. Fix Names in a Table · Easy · https://leetcode.com/problems/fix-names-in-a-table/
Plan: 30 Days of Pandas · Gün 7 · String Methods

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'name'], [[1, 'aLice'], [2, 'bOB']], {'user_id': 'Int64', 'name': 'object'})
    check(fix_names(users), ['user_id', 'name'], [[1, 'Alice'], [2, 'Bob']], ordered=True)
