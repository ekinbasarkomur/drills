"""
1667. Fix Names in a Table · Easy · https://leetcode.com/problems/fix-names-in-a-table/
Plan: 30 Days of Pandas · Gün 7 · String Methods

Problem: make only the first letter of each name upper case and the rest lower case; result sorted by user_id.
Approach: name.str[0].str.upper() + name.str[1:].str.lower(); every string step on a Series needs its own .str (str.capitalize() does both in one step), then sort by user_id
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users["name"] = users["name"].str[0].str.upper() + users["name"].str[1:].str.lower()
    return users.sort_values(by=["user_id"])


# ---------------------------------------------------------------- tests


def test_example_1():
    users = frame(
        ["user_id", "name"],
        [[1, "aLice"], [2, "bOB"]],
        {"user_id": "Int64", "name": "object"},
    )
    check(
        fix_names(users), ["user_id", "name"], [[1, "Alice"], [2, "Bob"]], ordered=True
    )


def test_unsorted_input():
    users = frame(
        ["user_id", "name"],
        [[2, "bOB"], [1, "aLice"]],
        {"user_id": "Int64", "name": "object"},
    )
    check(
        fix_names(users), ["user_id", "name"], [[1, "Alice"], [2, "Bob"]], ordered=True
    )
