"""
1907. Count Salary Categories · Medium · https://leetcode.com/problems/count-salary-categories/
Plan: 30 Days of Pandas · Gün 18 · Statistics

Problem: the number of accounts in each salary category (Low under 20000, Average 20000 to 50000 inclusive, High over 50000); every category must appear, even with a count of 0.
Approach: one boolean mask per category, the masked frame's row count (shape[0]) is that category's count; the three counts go into a fixed three-row DataFrame, so an empty category still shows 0.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low = accounts[accounts["income"] < 20000].shape[0]
    avg = accounts[(accounts["income"] >= 20000) & (accounts["income"] <= 50000)].shape[
        0
    ]
    high = accounts[accounts["income"] > 50000].shape[0]

    print(accounts)
    return pd.DataFrame(
        {
            "category": ["Low Salary", "Average Salary", "High Salary"],
            "accounts_count": [low, avg, high],
        }
    )


# ---------------------------------------------------------------- tests

# Three fixed categories, always all three rows, even when a category has no
# accounts (then its count is 0). Boundaries: 19999 is Low, 20000 and 50000
# are Average, 50001 is High. Any row order.

LOW, AVG, HIGH = "Low Salary", "Average Salary", "High Salary"


def accounts_with(*incomes):
    return frame(
        ["account_id", "income"],
        [[i + 1, inc] for i, inc in enumerate(incomes)],
        {"account_id": "Int64", "income": "Int64"},
    )


def test_example_1():
    accounts = frame(
        ["account_id", "income"],
        [[3, 108939], [2, 12747], [8, 87709], [6, 91796]],
        {"account_id": "Int64", "income": "Int64"},
    )
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 1], [AVG, 0], [HIGH, 3]],
    )


def test_boundaries_20000_and_50000_are_average():
    accounts = accounts_with(19999, 20000, 50000, 50001)
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 1], [AVG, 2], [HIGH, 1]],
    )


def test_missing_categories_still_appear_with_zero():
    accounts = accounts_with(30000, 40000)
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 0], [AVG, 2], [HIGH, 0]],
    )


def test_empty_table_gives_three_zeros():
    accounts = accounts_with()
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 0], [AVG, 0], [HIGH, 0]],
    )


def test_only_low():
    accounts = accounts_with(0, 1, 19999)
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 3], [AVG, 0], [HIGH, 0]],
    )


def test_same_income_counts_each_account():
    accounts = accounts_with(60000, 60000, 60000, 10000, 10000)
    check(
        count_salary_categories(accounts),
        ["category", "accounts_count"],
        [[LOW, 2], [AVG, 0], [HIGH, 3]],
    )
