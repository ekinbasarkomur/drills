"""
177. Nth Highest Salary · Medium · https://leetcode.com/problems/nth-highest-salary/
Plan: 30 Days of Pandas · Gün 10 · Data Manipulation

Problem: return the N-th highest distinct salary as a one-row frame whose column is named getNthHighestSalary(N); None when N is out of range or there are fewer than N distinct salaries.
Approach: drop duplicate salaries, sort them descending and take position N-1; N <= 0 or N beyond the distinct count returns the None row before indexing.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    column = "getNthHighestSalary({})".format(N)

    if N <= 0:
        return pd.DataFrame([None], columns=[column])

    salaries = employee["salary"].drop_duplicates()

    if N > len(salaries):
        return pd.DataFrame([None], columns=[column])

    salaries = salaries.sort_values(ascending=False)

    return pd.DataFrame([salaries.iloc[N - 1]], columns=[column])


# ---------------------------------------------------------------- tests

# The result is a one-row frame whose single column is named after the argument:
# getNthHighestSalary(2). Too few distinct salaries -> that one row holds None.


def salaries(*values):
    return frame(
        ["id", "salary"],
        [[i, v] for i, v in enumerate(values, start=1)],
        {"id": "int64", "salary": "int64"},
    )


def test_example_1():
    check(
        nth_highest_salary(salaries(100, 200, 300), 2),
        ["getNthHighestSalary(2)"],
        [[200]],
    )


def test_example_2():
    # only one salary, so there is no second highest
    check(
        nth_highest_salary(salaries(100), 2),
        ["getNthHighestSalary(2)"],
        [[None]],
    )


def test_n_is_one():
    check(
        nth_highest_salary(salaries(100, 300, 200), 1),
        ["getNthHighestSalary(1)"],
        [[300]],
    )


def test_duplicates_count_once():
    # distinct salaries are 300 and 100, so the 2nd highest is 100, not 300
    check(
        nth_highest_salary(salaries(300, 300, 100), 2),
        ["getNthHighestSalary(2)"],
        [[100]],
    )


def test_duplicates_can_leave_too_few():
    check(
        nth_highest_salary(salaries(100, 100), 2),
        ["getNthHighestSalary(2)"],
        [[None]],
    )


def test_n_larger_than_the_table():
    check(
        nth_highest_salary(salaries(100, 200), 5),
        ["getNthHighestSalary(5)"],
        [[None]],
    )


def test_n_is_zero():
    # not in the statement, but the judge asks for it
    check(
        nth_highest_salary(salaries(100, 200), 0),
        ["getNthHighestSalary(0)"],
        [[None]],
    )


def test_n_is_negative():
    # the judge has a hidden case with n = -1; slicing must not wrap around
    check(
        nth_highest_salary(salaries(100, 200, 300), -1),
        ["getNthHighestSalary(-1)"],
        [[None]],
    )


def test_empty_table():
    check(
        nth_highest_salary(salaries(), 1),
        ["getNthHighestSalary(1)"],
        [[None]],
    )


def test_the_lowest_distinct_salary():
    check(
        nth_highest_salary(salaries(100, 200, 300, 300), 3),
        ["getNthHighestSalary(3)"],
        [[100]],
    )
