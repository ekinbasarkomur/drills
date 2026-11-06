"""
3172. Second Day Verification · Easy · https://leetcode.com/problems/second-day-verification/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_second_day_signups(emails: pd.DataFrame, texts: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    emails = frame(['email_id', 'user_id', 'signup_date'], [[125, 7771, '2022-06-14 09:30:00'], [433, 1052, '2022-07-09 08:15:00'], [234, 7005, '2022-08-20 10:00:00']], {})
    texts = frame(['text_id', 'email_id', 'signup_action', 'action_date'], [[1, 125, 'Verified', '2022-06-15 08:30:00'], [2, 433, 'Not Verified', '2022-07-10 10:45:00'], [4, 234, 'Verified', '2022-08-21 09:30:00']], {})
    check(find_second_day_signups(emails, texts), ['user_id'], [[7005], [7771]], ordered=True)
