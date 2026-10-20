"""
1050. Actors and Directors Who Cooperated At Least Three Times · Easy · https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/
Plan: 30 Days of Pandas · Gün 26 · Data Integration

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    actor_director = frame(['actor_id', 'director_id', 'timestamp'], [[1, 1, 0], [1, 1, 1], [1, 1, 2], [1, 2, 3], [1, 2, 4], [2, 1, 5], [2, 1, 6]], {'actor_id': 'int64', 'director_id': 'int64', 'timestamp': 'int64'})
    check(actors_and_directors(actor_director), ['actor_id', 'director_id'], [[1, 1]], ordered=False)
