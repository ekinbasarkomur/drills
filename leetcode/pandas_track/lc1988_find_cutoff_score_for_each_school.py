"""
1988. Find Cutoff Score for Each School · Medium · https://leetcode.com/problems/find-cutoff-score-for-each-school/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_cutoff_score(schools: pd.DataFrame, exam: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    schools = frame(['school_id', 'capacity'], [[11, 151], [5, 48], [9, 9], [10, 99]], {'school_id': 'Int64', 'capacity': 'Int64'})
    exam = frame(['score', 'student_count'], [[975, 10], [966, 60], [844, 76], [749, 76], [744, 100]], {'score': 'Int64', 'student_count': 'Int64'})
    check(find_cutoff_score(schools, exam), ['school_id', 'score'], [[5, 975], [9, -1], [10, 749], [11, 744]], ordered=False)
