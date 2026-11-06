"""
2987. Find Expensive Cities · Easy · https://leetcode.com/problems/find-expensive-cities/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_expensive_cities(listings: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    listings = frame(['listing_id', 'city', 'price'], [[113, 'LosAngeles', 7560386], [136, 'SanFrancisco', 2380268], [92, 'Chicago', 9833209], [60, 'Chicago', 5147582], [8, 'Chicago', 5274441], [79, 'SanFrancisco', 8372065], [37, 'Chicago', 7939595], [53, 'LosAngeles', 4965123], [178, 'SanFrancisco', 999207], [51, 'NewYork', 5951718], [121, 'NewYork', 2893760]], {'listing_id': 'Int64', 'city': 'object', 'price': 'Int64'})
    check(find_expensive_cities(listings), ['city'], [['Chicago'], ['LosAngeles']], ordered=False)
