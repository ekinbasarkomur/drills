"""
1294. Weather Type in Each Country · Easy · https://leetcode.com/problems/weather-type-in-each-country/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def weather_type(countries: pd.DataFrame, weather: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    countries = frame(['country_id', 'country_name'], [[2, 'USA'], [3, 'Australia'], [7, 'Peru'], [5, 'China'], [8, 'Morocco'], [9, 'Spain']], {'country_id': 'Int64', 'country_name': 'object'})
    weather = frame(['country_id', 'weather_state', 'day'], [[2, 15, '2019-11-01'], [2, 12, '2019-10-28'], [2, 12, '2019-10-27'], [3, -2, '2019-11-10'], [3, 0, '2019-11-11'], [3, 3, '2019-11-12'], [5, 16, '2019-11-07'], [5, 18, '2019-11-09'], [5, 21, '2019-11-23'], [7, 25, '2019-11-28'], [7, 22, '2019-12-01'], [7, 20, '2019-12-02'], [8, 25, '2019-11-05'], [8, 27, '2019-11-15'], [8, 31, '2019-11-25'], [9, 7, '2019-10-23'], [9, 3, '2019-12-23']], {'country_id': 'Int64', 'weather_state': 'Int64', 'day': 'datetime64[ns]'})
    weather_type(countries, weather)
