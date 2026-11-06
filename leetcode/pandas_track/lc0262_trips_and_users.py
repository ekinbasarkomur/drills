"""
262. Trips and Users · Hard · https://leetcode.com/problems/trips-and-users/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    trips = frame(['id', 'client_id', 'driver_id', 'city_id', 'status', 'request_at'], [['1', '1', '10', '1', 'completed', '2013-10-01'], ['2', '2', '11', '1', 'cancelled_by_driver', '2013-10-01'], ['3', '3', '12', '6', 'completed', '2013-10-01'], ['4', '4', '13', '6', 'cancelled_by_client', '2013-10-01'], ['5', '1', '10', '1', 'completed', '2013-10-02'], ['6', '2', '11', '6', 'completed', '2013-10-02'], ['7', '3', '12', '6', 'completed', '2013-10-02'], ['8', '2', '12', '12', 'completed', '2013-10-03'], ['9', '3', '10', '12', 'completed', '2013-10-03'], ['10', '4', '13', '12', 'cancelled_by_driver', '2013-10-03']], {'id': 'Int64', 'client_id': 'Int64', 'driver_id': 'Int64', 'city_id': 'Int64', 'status': 'object', 'request_at': 'object'})
    users = frame(['users_id', 'banned', 'role'], [['1', 'No', 'client'], ['2', 'Yes', 'client'], ['3', 'No', 'client'], ['4', 'No', 'client'], ['10', 'No', 'driver'], ['11', 'No', 'driver'], ['12', 'No', 'driver'], ['13', 'No', 'driver']], {'users_id': 'Int64', 'banned': 'object', 'role': 'object'})
    check(trips_and_users(trips, users), ['Day', 'Cancellation Rate'], [['2013-10-01', 0.33], ['2013-10-02', 0.0], ['2013-10-03', 0.5]], ordered=False)
