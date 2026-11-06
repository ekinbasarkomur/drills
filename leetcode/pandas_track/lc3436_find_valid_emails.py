"""
3436. Find Valid Emails · Easy · https://leetcode.com/problems/find-valid-emails/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    users = frame(['user_id', 'email'], [[1, 'alice@example.com'], [2, 'bob_at_example.com'], [3, 'charlie@example.net'], [4, 'david@domain.com'], [5, 'eve@invalid']], {})
    check(find_valid_emails(users), ['user_id', 'email'], [[1, 'alice@example.com'], [4, 'david@domain.com']], ordered=True)
