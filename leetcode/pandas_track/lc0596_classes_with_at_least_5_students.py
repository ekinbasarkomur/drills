"""
596. Classes With at Least 5 Students · Easy · https://leetcode.com/problems/classes-with-at-least-5-students/
Plan: 30 Days of Pandas · Gün 22 · Data Aggregation

Problem: the classes that have at least five students, returned as a single class column.
Approach: groupby class and count the students, reset_index turns class back into a column, then a boolean mask keeps the counts of 5 or more (SQL's HAVING) and only the class column is returned.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:

    courses = pd.DataFrame(courses.groupby("class")["student"].count()).reset_index()
    return courses[courses["student"] >= 5][["class"]]


# ---------------------------------------------------------------- tests

# One column `class`, one row per class with 5 or more students. Exactly 5
# counts ("at least"), 4 does not. Any row order.


def enrolments(**classes):
    # enrolments(Math=6, English=1) -> 6 Math rows, 1 English row
    rows, n = [], 0
    for cls, k in classes.items():
        for _ in range(k):
            rows.append([f"s{n}", cls])
            n += 1
    return frame(["student", "class"], rows, {"student": "object", "class": "object"})


def test_example_1():
    courses = frame(
        ["student", "class"],
        [
            ["A", "Math"],
            ["B", "English"],
            ["C", "Math"],
            ["D", "Biology"],
            ["E", "Math"],
            ["F", "Computer"],
            ["G", "Math"],
            ["H", "Math"],
            ["I", "Math"],
        ],
        {"student": "object", "class": "object"},
    )
    check(find_classes(courses), ["class"], [["Math"]])


def test_exactly_five_is_included():
    courses = enrolments(Math=5)
    check(find_classes(courses), ["class"], [["Math"]])


def test_four_is_not():
    courses = enrolments(Math=4)
    check(find_classes(courses), ["class"], [])


def test_several_qualify():
    courses = enrolments(Math=5, Art=7, Music=2, Physics=6)
    check(find_classes(courses), ["class"], [["Math"], ["Art"], ["Physics"]])


def test_none_qualify():
    courses = enrolments(Math=1, Art=2, Music=3, Physics=4)
    check(find_classes(courses), ["class"], [])


def test_empty_table():
    courses = enrolments()
    check(find_classes(courses), ["class"], [])
