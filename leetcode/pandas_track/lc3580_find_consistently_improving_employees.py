"""
3580. Find Consistently Improving Employees · Medium · https://leetcode.com/problems/find-consistently-improving-employees/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_consistently_improving_employees(employees: pd.DataFrame, performance_reviews: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    employees = frame(['employee_id', 'name'], [[1, 'Alice Johnson'], [2, 'Bob Smith'], [3, 'Carol Davis'], [4, 'David Wilson'], [5, 'Emma Brown']], {})
    performance_reviews = frame(['review_id', 'employee_id', 'review_date', 'rating'], [[1, 1, '2023-01-15', 2], [2, 1, '2023-04-15', 3], [3, 1, '2023-07-15', 4], [4, 1, '2023-10-15', 5], [5, 2, '2023-02-01', 3], [6, 2, '2023-05-01', 2], [7, 2, '2023-08-01', 4], [8, 2, '2023-11-01', 5], [9, 3, '2023-03-10', 1], [10, 3, '2023-06-10', 2], [11, 3, '2023-09-10', 3], [12, 3, '2023-12-10', 4], [13, 4, '2023-01-20', 4], [14, 4, '2023-04-20', 4], [15, 4, '2023-07-20', 4], [16, 5, '2023-02-15', 3], [17, 5, '2023-05-15', 2]], {})
    check(find_consistently_improving_employees(employees, performance_reviews), ['employee_id', 'name', 'improvement_score'], [[2, 'Bob Smith', 3], [1, 'Alice Johnson', 2], [3, 'Carol Davis', 2]], ordered=True)
