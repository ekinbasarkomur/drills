"""
2356. Number of Unique Subjects Taught by Each Teacher · Easy · https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/
Plan: 30 Days of Pandas · Gün 21 · Data Aggregation

Problem: the number of unique subjects each teacher teaches; a subject taught in several departments counts once. Columns teacher_id and cnt.
Approach: groupby teacher_id and take nunique of subject_id, so a subject repeated across departments counts once; rename the column to cnt and reset_index turns teacher_id back into a column.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:

    return (
        pd.DataFrame(teacher.groupby("teacher_id")["subject_id"].nunique())
        .rename(columns={"subject_id": "cnt"})
        .reset_index()
    )


# ---------------------------------------------------------------- tests

# One row per teacher, `cnt` = how many DISTINCT subject_ids they teach. The
# same subject taught in two departments is two rows but one subject, so a
# plain row count is wrong. Any row order.


def teaches(*rows):
    return frame(
        ["teacher_id", "subject_id", "dept_id"],
        [list(r) for r in rows],
        {"teacher_id": "Int64", "subject_id": "Int64", "dept_id": "Int64"},
    )


COLS = ["teacher_id", "cnt"]


def test_example_1():
    teacher = teaches(
        (1, 2, 3),
        (1, 2, 4),
        (1, 3, 3),
        (2, 1, 1),
        (2, 2, 1),
        (2, 3, 1),
        (2, 4, 1),
    )
    check(count_unique_subjects(teacher), COLS, [[1, 2], [2, 4]])


def test_same_subject_in_many_departments_counts_once():
    teacher = teaches((1, 7, 1), (1, 7, 2), (1, 7, 3), (1, 7, 4))
    check(count_unique_subjects(teacher), COLS, [[1, 1]])


def test_all_different_subjects():
    teacher = teaches((1, 1, 1), (1, 2, 1), (1, 3, 1))
    check(count_unique_subjects(teacher), COLS, [[1, 3]])


def test_every_teacher_appears():
    teacher = teaches((1, 1, 1), (2, 1, 2), (3, 1, 3))
    check(count_unique_subjects(teacher), COLS, [[1, 1], [2, 1], [3, 1]])


def test_mixed():
    teacher = teaches(
        (5, 1, 1),
        (5, 1, 2),
        (5, 2, 1),
        (9, 3, 1),
    )
    check(count_unique_subjects(teacher), COLS, [[5, 2], [9, 1]])


def test_empty_table():
    teacher = teaches()
    check(count_unique_subjects(teacher), COLS, [])
