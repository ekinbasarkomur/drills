"""
2082. The Number of Rich Customers · Easy · https://leetcode.com/problems/the-number-of-rich-customers/
Plan: 30 Days of Pandas · Gün 16 · Statistics

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    return store


# ---------------------------------------------------------------- tests

# The answer is a one-row frame with a single column `rich_count`: how many
# distinct customers have at least one bill strictly over 500. One customer
# with five big bills still counts once.


def bills(*rows):
    return frame(
        ["bill_id", "customer_id", "amount"],
        [list(r) for r in rows],
        {"bill_id": "int64", "customer_id": "int64", "amount": "int64"},
    )


def test_example_1():
    store = bills((6, 1, 549), (8, 1, 834), (4, 2, 394), (11, 3, 657), (13, 3, 257))
    check(count_rich_customers(store), ["rich_count"], [[2]])


def test_one_customer_many_big_bills_counts_once():
    store = bills((1, 7, 600), (2, 7, 700), (3, 7, 800))
    check(count_rich_customers(store), ["rich_count"], [[1]])


def test_exactly_500_is_not_rich():
    store = bills((1, 1, 500), (2, 2, 501))
    check(count_rich_customers(store), ["rich_count"], [[1]])


def test_nobody_is_rich():
    store = bills((1, 1, 10), (2, 2, 20))
    check(count_rich_customers(store), ["rich_count"], [[0]])


def test_empty_table():
    store = bills()
    check(count_rich_customers(store), ["rich_count"], [[0]])


def test_everyone_is_rich():
    store = bills((1, 1, 999), (2, 2, 999), (3, 3, 999), (4, 3, 1))
    check(count_rich_customers(store), ["rich_count"], [[3]])
