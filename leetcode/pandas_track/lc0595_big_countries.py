"""
595. Big Countries · Easy · https://leetcode.com/problems/big-countries/
Plan: 30 Days of Pandas · Gün 1 · Data Filtering

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    world = frame(['name', 'continent', 'area', 'population', 'gdp'], [['Afghanistan', 'Asia', 652230, 25500100, 20343000000], ['Albania', 'Europe', 28748, 2831741, 12960000000], ['Algeria', 'Africa', 2381741, 37100000, 188681000000], ['Andorra', 'Europe', 468, 78115, 3712000000], ['Angola', 'Africa', 1246700, 20609294, 100990000000]], {'name': 'object', 'continent': 'object', 'area': 'Int64', 'population': 'Int64', 'gdp': 'Int64'})
    check(big_countries(world), ['name', 'population', 'area'], [['Afghanistan', 25500100, 652230], ['Algeria', 37100000, 2381741]], ordered=False)
