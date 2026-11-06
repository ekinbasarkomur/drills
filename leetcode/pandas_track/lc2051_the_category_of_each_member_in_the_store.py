"""
2051. The Category of Each Member in the Store · Medium · https://leetcode.com/problems/the-category-of-each-member-in-the-store/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_categories(members: pd.DataFrame, visits: pd.DataFrame, purchases: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    members = frame(['member_id', 'name'], [[9, 'Alice'], [11, 'Bob'], [3, 'Winston'], [8, 'Hercy'], [1, 'Narihan']], {'member_id': 'Int64', 'name': 'object'})
    visits = frame(['visit_id', 'member_id', 'visit_date'], [[22, 11, '2021-10-28'], [16, 11, '2021-01-12'], [18, 9, '2021-12-10'], [19, 3, '2021-10-19'], [12, 11, '2021-03-01'], [17, 8, '2021-05-07'], [21, 9, '2021-05-12']], {'visit_id': 'Int64', 'member_id': 'Int64', 'visit_date': 'datetime64[ns]'})
    purchases = frame(['visit_id', 'charged_amount'], [[12, 2000], [18, 9000], [17, 7000]], {'visit_id': 'Int64', 'charged_amount': 'Int64'})
    check(find_categories(members, visits, purchases), ['member_id', 'name', 'category'], [[1, 'Narihan', 'Bronze'], [3, 'Winston', 'Silver'], [8, 'Hercy', 'Diamond'], [9, 'Alice', 'Gold'], [11, 'Bob', 'Silver']], ordered=False)
