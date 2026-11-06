"""
1308. Running Total for Different Genders · Medium · https://leetcode.com/problems/running-total-for-different-genders/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def running_total(scores: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    scores = frame(['player_name', 'gender', 'day', 'score_points'], [['Aron', 'F', '2020-01-01', 17], ['Alice', 'F', '2020-01-07', 23], ['Bajrang', 'M', '2020-01-07', 7], ['Khali', 'M', '2019-12-25', 11], ['Slaman', 'M', '2019-12-30', 13], ['Joe', 'M', '2019-12-31', 3], ['Jose', 'M', '2019-12-18', 2], ['Priya', 'F', '2019-12-31', 23], ['Priyanka', 'F', '2019-12-30', 17]], {'player_name': 'object', 'gender': 'object', 'day': 'datetime64[ns]', 'score_points': 'Int64'})
    check(running_total(scores), ['gender', 'day', 'total'], [['F', '2019-12-30', 17], ['F', '2019-12-31', 40], ['F', '2020-01-01', 57], ['F', '2020-01-07', 80], ['M', '2019-12-18', 2], ['M', '2019-12-25', 13], ['M', '2019-12-30', 26], ['M', '2019-12-31', 29], ['M', '2020-01-07', 36]], ordered=True)
