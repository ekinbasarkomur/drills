"""
615. Average Salary: Departments VS Company · Hard · https://leetcode.com/problems/average-salary-departments-vs-company/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def average_salary(salary: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    salary = frame(['id', 'employee_id', 'amount', 'pay_date'], [[1, 1, 9000, '2017/03/31'], [2, 2, 6000, '2017/03/31'], [3, 3, 10000, '2017/03/31'], [4, 1, 7000, '2017/02/28'], [5, 2, 6000, '2017/02/28'], [6, 3, 8000, '2017/02/28']], {'id': 'Int64', 'employee_id': 'Int64', 'amount': 'Int64', 'pay_date': 'datetime64[ns]'})
    employee = frame(['employee_id', 'department_id'], [[1, 1], [2, 2], [3, 2]], {'employee_id': 'Int64', 'department_id': 'Int64'})
    check(average_salary(salary, employee), ['pay_month', 'department_id', 'comparison'], [['2017-02', 1, 'same'], ['2017-03', 1, 'higher'], ['2017-02', 2, 'same'], ['2017-03', 2, 'lower']], ordered=False)
