"""
184. Department Highest Salary · Medium · https://leetcode.com/problems/department-highest-salary/
Plan: 30 Days of Pandas · Gün 12 · Data Manipulation

Problem: list every employee who earns the top salary of their department as Department, Employee, Salary; ties give one row each.
Approach: compare each salary with its department maximum broadcast back by groupby transform, keep the matching rows, map departmentId to the department name and rename the columns.
Time O(n + m), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def department_highest_salary(
    employee: pd.DataFrame, department: pd.DataFrame
) -> pd.DataFrame:
    tops = employee["salary"] == employee.groupby("departmentId")["salary"].transform(
        "max"
    )
    result = employee[tops].copy()

    names = department.set_index("id")["name"]
    result["Department"] = employee["departmentId"].map(names)
    result = result.drop(columns=["id"])

    result = result.rename(columns={"name": "Employee", "salary": "Salary"})
    result = result[["Department", "Employee", "Salary"]]

    return result


# ---------------------------------------------------------------- tests

# The result has three columns, renamed: Department, Employee, Salary.
# Every employee on a department's top salary is listed, so a tie gives two rows.


def employees(*rows):
    """(name, salary, departmentId) triples, ids filled in."""
    return frame(
        ["id", "name", "salary", "departmentId"],
        [[i, n, s, d] for i, (n, s, d) in enumerate(rows, start=1)],
        {"id": "Int64", "name": "object", "salary": "Int64", "departmentId": "Int64"},
    )


def departments(*names):
    return frame(
        ["id", "name"],
        [[i, n] for i, n in enumerate(names, start=1)],
        {"id": "Int64", "name": "object"},
    )


def test_example_1():
    check(
        department_highest_salary(
            employees(
                ("Joe", 70000, 1),
                ("Jim", 90000, 1),
                ("Henry", 80000, 2),
                ("Sam", 60000, 2),
                ("Max", 90000, 1),
            ),
            departments("IT", "Sales"),
        ),
        ["Department", "Employee", "Salary"],
        [["IT", "Jim", 90000], ["Sales", "Henry", 80000], ["IT", "Max", 90000]],
        ordered=False,
    )


def test_a_tie_lists_everyone():
    # three employees on the same top salary, all three belong in the answer
    check(
        department_highest_salary(
            employees(("A", 500, 1), ("B", 500, 1), ("C", 500, 1), ("D", 100, 1)),
            departments("IT"),
        ),
        ["Department", "Employee", "Salary"],
        [["IT", "A", 500], ["IT", "B", 500], ["IT", "C", 500]],
        ordered=False,
    )


def test_every_department_is_represented():
    # one row per department, even when the highest salary is the lowest overall
    check(
        department_highest_salary(
            employees(("A", 10, 1), ("B", 20, 2), ("C", 30, 3)),
            departments("One", "Two", "Three"),
        ),
        ["Department", "Employee", "Salary"],
        [["One", "A", 10], ["Two", "B", 20], ["Three", "C", 30]],
        ordered=False,
    )


def test_an_empty_department_is_left_out():
    # Sales has no employees, so it must not appear at all
    check(
        department_highest_salary(
            employees(("A", 10, 1)),
            departments("IT", "Sales"),
        ),
        ["Department", "Employee", "Salary"],
        [["IT", "A", 10]],
        ordered=False,
    )


def test_single_employee():
    check(
        department_highest_salary(employees(("Solo", 1, 1)), departments("IT")),
        ["Department", "Employee", "Salary"],
        [["IT", "Solo", 1]],
        ordered=False,
    )


def test_two_departments_share_a_salary():
    # the same number is the top in both; neither department may be dropped
    check(
        department_highest_salary(
            employees(("A", 100, 1), ("B", 50, 1), ("C", 100, 2), ("D", 40, 2)),
            departments("IT", "Sales"),
        ),
        ["Department", "Employee", "Salary"],
        [["IT", "A", 100], ["Sales", "C", 100]],
        ordered=False,
    )


def test_departments_have_the_same_name_column_as_employees():
    # both tables carry a `name` column, so a careless merge renames them to
    # name_x / name_y and the output columns come out wrong
    check(
        department_highest_salary(
            employees(("IT", 10, 1)),
            departments("IT"),
        ),
        ["Department", "Employee", "Salary"],
        [["IT", "IT", 10]],
        ordered=False,
    )


def test_no_employees_at_all():
    check(
        department_highest_salary(employees(), departments("IT")),
        ["Department", "Employee", "Salary"],
        [],
        ordered=False,
    )
