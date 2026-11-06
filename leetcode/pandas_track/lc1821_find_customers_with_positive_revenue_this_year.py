"""
1821. Find Customers With Positive Revenue this Year · Easy · https://leetcode.com/problems/find-customers-with-positive-revenue-this-year/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_customers(customers: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'year', 'revenue'], [['1', '2018', '50'], ['1', '2021', '30'], ['1', '2020', '70'], ['2', '2021', '-50'], ['3', '2018', '10'], ['3', '2016', '50'], ['4', '2021', '20']], {'customer_id': 'Int64', 'year': 'Int64', 'revenue': 'Int64'})
    check(find_customers(customers), ['customer_id'], [[1], [4]], ordered=False)
