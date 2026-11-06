"""
3204. Bitwise User Permissions Analysis · Medium · https://leetcode.com/problems/bitwise-user-permissions-analysis/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def analyze_permissions(user_permissions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    user_permissions = frame(['user_id', 'permissions'], [[1, 5], [2, 12], [3, 7], [4, 3]], {})
    check(analyze_permissions(user_permissions), ['common_perms', 'any_perms'], [[0, 15]], ordered=False)
