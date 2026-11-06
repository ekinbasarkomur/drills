"""
574. Winning Candidate · Medium · https://leetcode.com/problems/winning-candidate/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def winning_candidate(candidate: pd.DataFrame, vote: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    candidate = frame(['id', 'name'], [[1, 'A'], [2, 'B'], [3, 'C'], [4, 'D'], [5, 'E']], {'id': 'Int64', 'name': 'object'})
    vote = frame(['id', 'candidateId'], [[1, 2], [2, 4], [3, 3], [4, 2], [5, 5]], {'id': 'Int64', 'candidateId': 'Int64'})
    check(winning_candidate(candidate, vote), ['name'], [['B']], ordered=False)
