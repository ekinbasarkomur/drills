"""
2504. Concatenate the Name and the Profession · Easy · https://leetcode.com/problems/concatenate-the-name-and-the-profession/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def concatenate_info(person: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    person = frame(['person_id', 'name', 'profession'], [[1, 'Alex', 'Singer'], [3, 'Alice', 'Actor'], [2, 'Bob', 'Player'], [4, 'Messi', 'Doctor'], [6, 'Tyson', 'Engineer'], [5, 'Meir', 'Lawyer']], {'person_id': 'Int64', 'name': 'object', 'profession': 'object'})
    check(concatenate_info(person), ['person_id', 'name'], [[6, 'Tyson(E)'], [5, 'Meir(L)'], [4, 'Messi(D)'], [3, 'Alice(A)'], [2, 'Bob(P)'], [1, 'Alex(S)']], ordered=True)
