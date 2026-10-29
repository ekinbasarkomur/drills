"""
1527. Patients With a Condition · Easy · https://leetcode.com/problems/patients-with-a-condition/
Plan: 30 Days of Pandas · Gün 9 · String Methods

Problem: return the patients that have a condition code starting with DIAB1; codes are separated by spaces.
Approach: a boolean mask with str.contains(r"(?:^| )DIAB1"): the code must sit at the start of the string or right after a space. \b would wrongly accept "+DIAB100"
Time O(n·L), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    return patients[patients["conditions"].str.contains(r"(?:^| )DIAB1")]


# ---------------------------------------------------------------- tests


def test_example_1():
    patients = frame(
        ["patient_id", "patient_name", "conditions"],
        [
            [1, "Daniel", "YFEV COUGH"],
            [2, "Alice", ""],
            [3, "Bob", "DIAB100 MYOP"],
            [4, "George", "ACNE DIAB100"],
            [5, "Alain", "DIAB201"],
            [6, "Nadia", "ACNE +DIAB100"],
            [7, "Omar", "XDIAB100"],
        ],
        {"patient_id": "int64", "patient_name": "object", "conditions": "object"},
    )
    check(
        find_patients(patients),
        ["patient_id", "patient_name", "conditions"],
        [[3, "Bob", "DIAB100 MYOP"], [4, "George", "ACNE DIAB100"]],
        ordered=False,
    )
