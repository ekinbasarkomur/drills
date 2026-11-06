"""
1571. Warehouse Manager · Easy · https://leetcode.com/problems/warehouse-manager/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def warehouse_manager(warehouse: pd.DataFrame, products: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    warehouse = frame(['name', 'product_id', 'units'], [['LCHouse1', 1, 1], ['LCHouse1', 2, 10], ['LCHouse1', 3, 5], ['LCHouse2', 1, 2], ['LCHouse2', 2, 2], ['LCHouse3', 4, 1]], {'name': 'object', 'product_id': 'Int64', 'units': 'Int64'})
    products = frame(['product_id', 'product_name', 'Width', 'Length', 'Height'], [[1, 'LC-TV', 5, 50, 40], [2, 'LC-KeyChain', 5, 5, 5], [3, 'LC-Phone', 2, 10, 10], [4, 'LC-T-Shirt', 4, 10, 20]], {'product_id': 'Int64', 'product_name': 'object', 'Width': 'Int64', 'Length': 'Int64', 'Height': 'Int64'})
    check(warehouse_manager(warehouse, products), ['warehouse_name', 'volume'], [['LCHouse1', 12250], ['LCHouse2', 20250], ['LCHouse3', 800]], ordered=False)
