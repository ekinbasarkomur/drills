"""
1693. Daily Leads and Partners · Easy · https://leetcode.com/problems/daily-leads-and-partners/
Plan: Paralel hat · Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    daily_sales = frame(['date_id', 'make_name', 'lead_id', 'partner_id'], [['2020-12-8', 'toyota', 0, 1], ['2020-12-8', 'toyota', 1, 0], ['2020-12-8', 'toyota', 1, 2], ['2020-12-7', 'toyota', 0, 2], ['2020-12-7', 'toyota', 0, 1], ['2020-12-8', 'honda', 1, 2], ['2020-12-8', 'honda', 2, 1], ['2020-12-7', 'honda', 0, 1], ['2020-12-7', 'honda', 1, 2], ['2020-12-7', 'honda', 2, 1]], {'date_id': 'datetime64[ns]', 'make_name': 'object', 'lead_id': 'Int64', 'partner_id': 'Int64'})
    check(daily_leads_and_partners(daily_sales), ['date_id', 'make_name', 'unique_leads', 'unique_partners'], [['2020-12-8', 'toyota', 2, 3], ['2020-12-7', 'toyota', 1, 2], ['2020-12-8', 'honda', 2, 2], ['2020-12-7', 'honda', 3, 2]], ordered=False)
