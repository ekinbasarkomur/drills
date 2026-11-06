"""
3198. Find Cities in Each State · Easy · https://leetcode.com/problems/find-cities-in-each-state/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_cities(cities: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    cities = frame(['state', 'city'], [['California', 'Los Angeles'], ['California', 'San Francisco'], ['California', 'San Diego'], ['Texas', 'Houston'], ['Texas', 'Austin'], ['Texas', 'Dallas'], ['New York', 'New York City'], ['New York', 'Buffalo'], ['New York', 'Rochester']], {})
    check(find_cities(cities), ['state', 'cities'], [['California', 'Los Angeles, San Diego, San Francisco'], ['New York', 'Buffalo, New York City, Rochester'], ['Texas', 'Austin, Dallas, Houston']], ordered=True)
