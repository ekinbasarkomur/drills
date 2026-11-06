"""
3166. Calculate Parking Fees and Duration · Medium · https://leetcode.com/problems/calculate-parking-fees-and-duration/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def calculate_fees_and_duration(parking_transactions: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    parking_transactions = frame(['lot_id', 'car_id', 'entry_time', 'exit_time', 'fee_paid'], [[1, 1001, '2023-06-01 08:00:00', '2023-06-01 10:30:00', 5.0], [1, 1001, '2023-06-02 11:00:00', '2023-06-02 12:45:00', 3.0], [2, 1001, '2023-06-01 10:45:00', '2023-06-01 12:00:00', 6.0], [2, 1002, '2023-06-01 09:00:00', '2023-06-01 11:30:00', 4.0], [3, 1001, '2023-06-03 07:00:00', '2023-06-03 09:00:00', 4.0], [3, 1002, '2023-06-02 12:00:00', '2023-06-02 14:00:00', 2.0]], {})
    check(calculate_fees_and_duration(parking_transactions), ['car_id', 'total_fee_paid', 'avg_hourly_fee', 'most_time_lot'], [[1001, 18.0, 2.4, 1], [1002, 6.0, 1.33, 2]], ordered=True)
