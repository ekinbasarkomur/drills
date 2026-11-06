"""
3328. Find Cities in Each State II · Medium · https://leetcode.com/problems/find-cities-in-each-state-ii/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def state_city_analysis(cities: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    cities = frame(['state', 'city'], [['New York', 'New York City'], ['New York', 'Newark'], ['New York', 'Buffalo'], ['New York', 'Rochester'], ['California', 'San Francisco'], ['California', 'Sacramento'], ['California', 'San Diego'], ['California', 'Los Angeles'], ['Texas', 'Tyler'], ['Texas', 'Temple'], ['Texas', 'Taylor'], ['Texas', 'Dallas'], ['Pennsylvania', 'Philadelphia'], ['Pennsylvania', 'Pittsburgh'], ['Pennsylvania', 'Pottstown']], {})
    check(state_city_analysis(cities), ['state', 'cities', 'matching_letter_count'], [['Pennsylvania', 'Philadelphia, Pittsburgh, Pottstown', 3], ['Texas', 'Dallas, Taylor, Temple, Tyler', 3], ['New York', 'Buffalo, Newark, New York City, Rochester', 2]], ordered=True)
