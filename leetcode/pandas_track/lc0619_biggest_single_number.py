"""
619. Biggest Single Number · Easy · https://leetcode.com/problems/biggest-single-number/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    my_numbers = frame(['num'], [[8], [8], [3], [3], [1], [4], [5], [6]], {'num': 'Int64'})
    check(biggest_single_number(my_numbers), ['num'], [[6]], ordered=False)


def test_example_2():
    my_numbers = frame(['num'], [[8], [8], [7], [7], [3], [3], [3]], {'num': 'Int64'})
    check(biggest_single_number(my_numbers), ['num'], [[None]], ordered=False)
