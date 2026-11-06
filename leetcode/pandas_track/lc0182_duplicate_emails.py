"""
182. Duplicate Emails · Easy · https://leetcode.com/problems/duplicate-emails/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    person = frame(['id', 'email'], [[1, 'a@b.com'], [2, 'c@d.com'], [3, 'a@b.com']], {'id': 'Int64', 'email': 'object'})
    check(duplicate_emails(person), ['Email'], [['a@b.com']], ordered=False)
