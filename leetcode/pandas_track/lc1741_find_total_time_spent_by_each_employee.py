"""
1741. Find Total Time Spent by Each Employee · Easy · https://leetcode.com/problems/find-total-time-spent-by-each-employee/
Plan: 30 Days of Pandas · Gün 19 · Data Aggregation

Problem: the total time each employee spent in the office on each day, the sum of out_time - in_time over all their visits that day; the output columns are day, emp_id, total_time.
Approach: rename event_day to day, a per-visit duration column (out_time - in_time), then groupby on the two keys (day, emp_id) and sum the durations; the two keys form a MultiIndex, reset_index turns them back into columns.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.rename(columns={"event_day": "day"})
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    group = employees.groupby(["day", "emp_id"])
    return pd.DataFrame(group["total_time"].sum()).reset_index()


# ---------------------------------------------------------------- tests

# One row per (day, employee): the sum of out_time - in_time over that
# employee's visits that day. Note the output column is `day`, not
# `event_day`, and the column order is day, emp_id, total_time. Any row order.


def events(*rows):
    return frame(
        ["emp_id", "event_day", "in_time", "out_time"],
        [list(r) for r in rows],
        {
            "emp_id": "Int64",
            "event_day": "datetime64[ns]",
            "in_time": "Int64",
            "out_time": "Int64",
        },
    )


COLS = ["day", "emp_id", "total_time"]


def test_example_1():
    employees = events(
        (1, "2020-11-28", 4, 32),
        (1, "2020-11-28", 55, 200),
        (1, "2020-12-03", 1, 42),
        (2, "2020-11-28", 3, 33),
        (2, "2020-12-09", 47, 74),
    )
    check(
        total_time(employees),
        COLS,
        [
            ["2020-11-28", 1, 173],
            ["2020-11-28", 2, 30],
            ["2020-12-03", 1, 41],
            ["2020-12-09", 2, 27],
        ],
    )


def test_one_visit_per_day():
    employees = events((1, "2021-01-01", 10, 20))
    check(total_time(employees), COLS, [["2021-01-01", 1, 10]])


def test_many_visits_same_day_are_summed():
    employees = events(
        (1, "2021-01-01", 1, 2),
        (1, "2021-01-01", 10, 20),
        (1, "2021-01-01", 100, 130),
    )
    check(total_time(employees), COLS, [["2021-01-01", 1, 41]])


def test_same_employee_different_days_stay_separate():
    employees = events(
        (1, "2021-01-01", 1, 11),
        (1, "2021-01-02", 1, 21),
    )
    check(
        total_time(employees),
        COLS,
        [["2021-01-01", 1, 10], ["2021-01-02", 1, 20]],
    )


def test_different_employees_same_day_stay_separate():
    employees = events(
        (1, "2021-01-01", 1, 11),
        (2, "2021-01-01", 1, 21),
        (3, "2021-01-01", 5, 6),
    )
    check(
        total_time(employees),
        COLS,
        [["2021-01-01", 1, 10], ["2021-01-01", 2, 20], ["2021-01-01", 3, 1]],
    )


def test_full_day():
    employees = events((7, "2021-06-15", 1, 1440))
    check(total_time(employees), COLS, [["2021-06-15", 7, 1439]])


def test_empty_table():
    employees = events()
    check(total_time(employees), COLS, [])
