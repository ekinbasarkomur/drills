"""
2041. Accepted Candidates From the Interviews · Medium · https://leetcode.com/problems/accepted-candidates-from-the-interviews/
Plan: 30 Days of Pandas · pekiştirme · Data Integration

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def accepted_candidates(candidates: pd.DataFrame, rounds: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    candidates = frame(['candidate_id', 'name', 'years_of_exp', 'interview_id'], [[11, 'Atticus', 1, 101], [9, 'Ruben', 6, 104], [6, 'Aliza', 10, 109], [8, 'Alfredo', 0, 107]], {'candidate_id': 'Int64', 'name': 'object', 'years_of_exp': 'Int64', 'interview_id': 'Int64'})
    rounds = frame(['interview_id', 'round_id', 'score'], [[109, 3, 4], [101, 2, 8], [109, 4, 1], [107, 1, 3], [104, 3, 6], [109, 1, 4], [104, 4, 7], [104, 1, 2], [109, 2, 1], [104, 2, 7], [107, 2, 3], [101, 1, 8]], {'interview_id': 'Int64', 'round_id': 'Int64', 'score': 'Int64'})
    accepted_candidates(candidates, rounds)
