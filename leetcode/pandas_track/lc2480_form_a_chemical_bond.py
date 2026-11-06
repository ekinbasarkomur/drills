"""
2480. Form a Chemical Bond · Easy · https://leetcode.com/problems/form-a-chemical-bond/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def form_bond(elements: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    elements = frame(['symbol', 'type', 'electrons'], [['He', 'Noble', 0], ['Na', 'Metal', 1], ['Ca', 'Metal', 2], ['La', 'Metal', 3], ['Cl', 'Nonmetal', 1], ['O', 'Nonmetal', 2], ['N', 'Nonmetal', 3]], {'symbol': 'object', 'type': 'object', 'electrons': 'Int64'})
    check(form_bond(elements), ['metal', 'nonmetal'], [['La', 'Cl'], ['Ca', 'Cl'], ['Na', 'Cl'], ['La', 'O'], ['Ca', 'O'], ['Na', 'O'], ['La', 'N'], ['Ca', 'N'], ['Na', 'N']], ordered=False)
