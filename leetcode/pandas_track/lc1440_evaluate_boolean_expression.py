"""
1440. Evaluate Boolean Expression · Medium · https://leetcode.com/problems/evaluate-boolean-expression/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def eval_expression(variables: pd.DataFrame, expressions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    variables = frame(['name', 'value'], [['x', 66], ['y', 77]], {'name': 'object', 'value': 'Int64'})
    expressions = frame(['left_operand', 'operator', 'right_operand'], [['x', '>', 'y'], ['x', '<', 'y'], ['x', '=', 'y'], ['y', '>', 'x'], ['y', '<', 'x'], ['x', '=', 'x']], {'left_operand': 'object', 'operator': 'object', 'right_operand': 'object'})
    check(eval_expression(variables, expressions), ['left_operand', 'operator', 'right_operand', 'value'], [['x', '>', 'y', 'false'], ['x', '<', 'y', 'true'], ['x', '=', 'y', 'false'], ['y', '>', 'x', 'true'], ['y', '<', 'x', 'false'], ['x', '=', 'x', 'true']], ordered=False)
