"""
1873. Calculate Special Bonus · Easy · https://leetcode.com/problems/calculate-special-bonus/
Plan: 30 Days of Pandas · Gün 6 · String Methods

Problem: bonus = salary if the id is odd and the name does not start with 'M', else 0; result sorted by employee_id.
Approach: salary.where(odd id & name.str[0] != 'M', 0) keeps the salary where the mask is True and writes 0 elsewhere, then sort by employee_id
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"].where(
        (employees["employee_id"] % 2 != 0) & (employees["name"].str[0] != "M"), 0
    )
    return employees[["employee_id", "bonus"]].sort_values(by=["employee_id"])


# ---------------------------------------------------------------- tests


def test_example_1():
    employees = frame(
        ["employee_id", "name", "salary"],
        [
            [2, "Meir", 3000],
            [3, "Michael", 3800],
            [7, "Addilyn", 7400],
            [8, "Juan", 6100],
            [9, "Kannon", 7700],
        ],
        {"employee_id": "int64", "name": "object", "salary": "int64"},
    )
    check(
        calculate_special_bonus(employees),
        ["employee_id", "bonus"],
        [[2, 0], [3, 0], [7, 7400], [8, 0], [9, 7700]],
        ordered=True,
    )


def test_unsorted_input():
    # LeetCode'un gizli testinde girdi sıralı değil; sonuç employee_id'ye göre sıralı istenir
    employees = frame(["employee_id", "name", "salary"], [[9, "Kannon", 7700], [2, "Meir", 3000], [3, "Michael", 3800]])
    check(calculate_special_bonus(employees), ["employee_id", "bonus"], [[2, 0], [3, 0], [9, 7700]], ordered=True)
