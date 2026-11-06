"""
3451. Find Invalid IP Addresses · Hard · https://leetcode.com/problems/find-invalid-ip-addresses/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_invalid_ips(logs: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    logs = frame(['log_id', 'ip', 'status_code'], [[8, '127.0.0.1', 200], [9, '192.168.1', 400]], {})
    check(find_invalid_ips(logs), ['ip', 'invalid_count'], [['256.1.2.3', 2], ['192.168.001.1', 2], ['192.168.1', 1]], ordered=True)
