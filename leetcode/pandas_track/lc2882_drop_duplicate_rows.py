"""
2882. Drop Duplicate Rows · Easy · https://leetcode.com/problems/drop-duplicate-rows/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers = customers.drop_duplicates(subset=["email"], keep="first", inplace=False)
    return customers


# ---------------------------------------------------------------- tests


def test_example_1():
    customers = frame(
        ["customer_id", "name", "email"],
        [
            [1, "Ella", "emily@example.com"],
            [2, "David", "michael@example.com"],
            [3, "Zachary", "sarah@example.com"],
            [4, "Alice", "john@example.com"],
            [5, "Finn", "john@example.com"],
            [6, "Violet", "alice@example.com"],
        ],
        {"customer_id": "Int64", "name": "object", "email": "object"},
    )
    check(
        dropDuplicateEmails(customers),
        ["customer_id", "name", "email"],
        [
            [1, "Ella", "emily@example.com"],
            [2, "David", "michael@example.com"],
            [3, "Zachary", "sarah@example.com"],
            [4, "Alice", "john@example.com"],
            [6, "Violet", "alice@example.com"],
        ],
        ordered=False,
    )
