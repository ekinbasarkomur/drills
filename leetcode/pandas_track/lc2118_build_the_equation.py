"""
2118. Build the Equation · Hard · https://leetcode.com/problems/build-the-equation/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def build_the_equation(terms: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    terms = frame(['power', 'factor'], [[2, 1], [1, -4], [0, 2]], {'power': 'Int64', 'factor': 'Int64'})
    check(build_the_equation(terms), ['equation'], [['+1X^2-4X+2=0']], ordered=False)


def test_example_2():
    terms = frame(['power', 'factor'], [[4, -4], [2, 1], [1, -1]], {'power': 'Int64', 'factor': 'Int64'})
    check(build_the_equation(terms), ['equation'], [['-4X^4+1X^2-1X=0']], ordered=False)
