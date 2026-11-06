"""
1811. Find Interview Candidates · Medium · https://leetcode.com/problems/find-interview-candidates/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_interview_candidates(contests: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    contests = frame(['contest_id', 'gold_medal', 'silver_medal', 'bronze_medal'], [[190, 1, 5, 2], [191, 2, 3, 5], [192, 5, 2, 3], [193, 1, 3, 5], [194, 4, 5, 2], [195, 4, 2, 1], [196, 1, 5, 2]], {'contest_id': 'Int64', 'gold_medal': 'Int64', 'silver_medal': 'Int64', 'bronze_medal': 'Int64'})
    users = frame(['user_id', 'mail', 'name'], [[1, 'sarah@leetcode.com', 'Sarah'], [2, 'bob@leetcode.com', 'Bob'], [3, 'alice@leetcode.com', 'Alice'], [4, 'hercy@leetcode.com', 'Hercy'], [5, 'quarz@leetcode.com', 'Quarz']], {'user_id': 'Int64', 'mail': 'object', 'name': 'object'})
    check(find_interview_candidates(contests, users), ['name', 'mail'], [['Sarah', 'sarah@leetcode.com'], ['Bob', 'bob@leetcode.com'], ['Alice', 'alice@leetcode.com'], ['Quarz', 'quarz@leetcode.com']], ordered=False)
