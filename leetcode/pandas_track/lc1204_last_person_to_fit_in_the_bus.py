"""
1204. Last Person to Fit in the Bus · Medium · https://leetcode.com/problems/last-person-to-fit-in-the-bus/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    queue = frame(['person_id', 'person_name', 'weight', 'turn'], [[5, 'Alice', 250, 1], [4, 'Bob', 175, 5], [3, 'Alex', 350, 2], [6, 'John Cena', 400, 3], [1, 'Winston', 500, 6], [2, 'Marie', 200, 4]], {'person_id': 'Int64', 'person_name': 'object', 'weight': 'Int64', 'turn': 'Int64'})
    check(last_passenger(queue), ['person_name'], [['John Cena']], ordered=True)
