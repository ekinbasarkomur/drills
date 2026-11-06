"""
1225. Report Contiguous Dates · Hard · https://leetcode.com/problems/report-contiguous-dates/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def report_contiguous_dates(failed: pd.DataFrame, succeeded: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    failed = frame(['fail_date'], [['2018-12-28'], ['2018-12-29'], ['2019-01-04'], ['2019-01-05']], {'fail_date': 'datetime64[ns]'})
    succeeded = frame(['success_date'], [['2018-12-30'], ['2018-12-31'], ['2019-01-01'], ['2019-01-02'], ['2019-01-03'], ['2019-01-06']], {'success_date': 'datetime64[ns]'})
    check(report_contiguous_dates(failed, succeeded), ['period_state', 'start_date', 'end_date'], [['succeeded', '2019-01-01', '2019-01-03'], ['failed', '2019-01-04', '2019-01-05'], ['succeeded', '2019-01-06', '2019-01-06']], ordered=True)
