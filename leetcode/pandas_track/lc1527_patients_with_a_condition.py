"""
1527. Patients With a Condition · Easy · https://leetcode.com/problems/patients-with-a-condition/
Plan: 30 Days of Pandas · Gün 9 · String Methods

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    patients = frame(['patient_id', 'patient_name', 'conditions'], [[1, 'Daniel', 'YFEV COUGH'], [2, 'Alice', ''], [3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100'], [5, 'Alain', 'DIAB201']], {'patient_id': 'int64', 'patient_name': 'object', 'conditions': 'object'})
    check(find_patients(patients), ['patient_id', 'patient_name', 'conditions'], [[3, 'Bob', 'DIAB100 MYOP'], [4, 'George', 'ACNE DIAB100']], ordered=False)
