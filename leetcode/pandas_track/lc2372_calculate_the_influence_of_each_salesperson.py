"""
2372. Calculate the Influence of Each Salesperson · Medium · https://leetcode.com/problems/calculate-the-influence-of-each-salesperson/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_influence(salesperson: pd.DataFrame, customer: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    salesperson = frame(['salesperson_id', 'name'], [[1, 'Alice'], [2, 'Bob'], [3, 'Jerry']], {'salesperson_id': 'Int64', 'name': 'object'})
    customer = frame(['customer_id', 'salesperson_id'], [[1, 1], [2, 1], [3, 2]], {'customer_id': 'Int64', 'salesperson_id': 'Int64'})
    sales = frame(['sale_id', 'customer_id', 'price'], [[1, 2, 892], [2, 1, 354], [3, 3, 988], [4, 3, 856]], {'sale_id': 'Int64', 'customer_id': 'Int64', 'price': 'Int64'})
    check(calculate_influence(salesperson, customer, sales), ['salesperson_id', 'name', 'total'], [[1, 'Alice', 1246], [2, 'Bob', 1844], [3, 'Jerry', 0]], ordered=False)
