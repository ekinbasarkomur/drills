"""
3051. Find Candidates for Data Scientist Position · Easy · https://leetcode.com/problems/find-candidates-for-data-scientist-position/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_candidates(candidates: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    candidates = frame(['candidate_id', 'skill'], [[123, 'Python'], [234, 'R'], [123, 'Tableau'], [123, 'PostgreSQL'], [234, 'PowerBI'], [234, 'SQL Server'], [147, 'Python'], [147, 'Tableau'], [147, 'Java'], [147, 'PostgreSQL'], [256, 'Tableau'], [102, 'DataAnalysis']], {'candidate_id': 'Int64', 'skill': 'object'})
    check(find_candidates(candidates), ['candidate_id'], [[123], [147]], ordered=True)
