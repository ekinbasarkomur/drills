"""
1501. Countries You Can Safely Invest In · Medium · https://leetcode.com/problems/countries-you-can-safely-invest-in/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_safe_countries(person: pd.DataFrame, country: pd.DataFrame, calls: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    person = frame(['id', 'name', 'phone_number'], [[3, 'Jonathan', '051-1234567'], [12, 'Elvis', '051-7654321'], [1, 'Moncef', '212-1234567'], [2, 'Maroua', '212-6523651'], [7, 'Meir', '972-1234567'], [9, 'Rachel', '972-0011100']], {'id': 'Int64', 'name': 'object', 'phone_number': 'object'})
    country = frame(['name', 'country_code'], [['Peru', '051'], ['Israel', '972'], ['Morocco', '212'], ['Germany', '049'], ['Ethiopia', '251']], {'name': 'object', 'country_code': 'object'})
    calls = frame(['caller_id', 'callee_id', 'duration'], [[1, 9, 33], [2, 9, 4], [1, 2, 59], [3, 12, 102], [3, 12, 330], [12, 3, 5], [7, 9, 13], [7, 1, 3], [9, 7, 1], [1, 7, 7]], {'caller_id': 'Int64', 'callee_id': 'Int64', 'duration': 'Int64'})
    check(find_safe_countries(person, country, calls), ['country'], [['Peru']], ordered=False)
