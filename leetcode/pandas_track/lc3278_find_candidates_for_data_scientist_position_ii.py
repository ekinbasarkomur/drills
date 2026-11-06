"""
3278. Find Candidates for Data Scientist Position II · Medium · https://leetcode.com/problems/find-candidates-for-data-scientist-position-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_best_candidates(candidates: pd.DataFrame, projects: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    candidates = frame(['candidate_id', 'skill', 'proficiency'], [[101, 'Python', 5], [101, 'Tableau', 3], [101, 'PostgreSQL', 4], [101, 'TensorFlow', 2], [102, 'Python', 4], [102, 'Tableau', 5], [102, 'PostgreSQL', 4], [102, 'R', 4], [103, 'Python', 3], [103, 'Tableau', 5], [103, 'PostgreSQL', 5], [103, 'Spark', 4]], {})
    projects = frame(['project_id', 'skill', 'importance'], [[501, 'Python', 4], [501, 'Tableau', 3], [501, 'PostgreSQL', 5], [502, 'Python', 3], [502, 'Tableau', 4], [502, 'R', 2]], {})
    check(find_best_candidates(candidates, projects), ['project_id', 'candidate_id', 'score'], [[501, 101, 105], [502, 102, 130]], ordered=True)
