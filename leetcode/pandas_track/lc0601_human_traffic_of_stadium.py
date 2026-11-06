"""
601. Human Traffic of Stadium · Hard · https://leetcode.com/problems/human-traffic-of-stadium/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    stadium = frame(['id', 'visit_date', 'people'], [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]], {'id': 'Int64', 'visit_date': 'datetime64[ns]', 'people': 'Int64'})
    check(human_traffic(stadium), ['id', 'visit_date', 'people'], [[5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]], ordered=True)
