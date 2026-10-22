"""
183. Customers Who Never Order · Easy · https://leetcode.com/problems/customers-who-never-order/
Plan: 30 Days of Pandas · Gün 3 · Data Filtering

Problem:
Approach:
Time O(?), space O(?)
"""

# ---------------------------------------------------------------- solution
import pandas as pd
from _pd import check, frame


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:

    customers = customers.merge(orders, on="id", how="left")
    customers = customers[customers["customerId"].isna()]
    customers = customers[["name"]]
    customers.columns = ["Customers"]
    return customers


# ---------------------------------------------------------------- tests


def test_example_1():
    customers = frame(
        ["id", "name"],
        [[1, "Joe"], [2, "Henry"], [3, "Sam"], [4, "Max"]],
        {"id": "Int64", "name": "object"},
    )
    orders = frame(
        ["id", "customerId"], [[1, 3], [2, 1]], {"id": "Int64", "customerId": "Int64"}
    )
    check(
        find_customers(customers, orders),
        ["Customers"],
        [["Henry"], ["Max"]],
        ordered=False,
    )
