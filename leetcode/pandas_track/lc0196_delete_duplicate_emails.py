"""
196. Delete Duplicate Emails · Easy · https://leetcode.com/problems/delete-duplicate-emails/
Plan: 30 Days of Pandas · Gün 14 · Data Manipulation

Problem: delete every row whose email already appears on a row with a smaller id, modifying the frame in place and returning nothing.
Approach: sort by id in place so the smallest id comes first, then drop_duplicates on email in place keeps the first occurrence per email.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by="id", inplace=True)
    person.drop_duplicates(subset=["email"], inplace=True)


# ---------------------------------------------------------------- tests

# The judge ignores what the function returns and looks at `person` itself
# afterwards, so these tests do the same: call, then check the frame that was
# passed in. Returning a new frame without touching `person` fails here, as it
# does on LeetCode.


def people(*rows):
    return frame(
        ["id", "email"], [list(r) for r in rows], {"id": "Int64", "email": "object"}
    )


def test_example_1():
    person = people(
        (1, "john@example.com"), (2, "bob@example.com"), (3, "john@example.com")
    )
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[1, "john@example.com"], [2, "bob@example.com"]])


def test_keeps_the_smallest_id_not_the_first_row():
    # rows arrive out of id order; the survivor must still be id 1
    person = people((3, "a@x.com"), (1, "a@x.com"), (2, "a@x.com"))
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[1, "a@x.com"]])


def test_no_duplicates_changes_nothing():
    person = people((1, "a@x.com"), (2, "b@x.com"), (3, "c@x.com"))
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[1, "a@x.com"], [2, "b@x.com"], [3, "c@x.com"]])


def test_every_row_is_the_same_email():
    person = people((5, "a@x.com"), (4, "a@x.com"), (6, "a@x.com"))
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[4, "a@x.com"]])


def test_several_duplicate_groups():
    person = people(
        (1, "a@x.com"),
        (2, "b@x.com"),
        (3, "a@x.com"),
        (4, "c@x.com"),
        (5, "b@x.com"),
        (6, "a@x.com"),
    )
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[1, "a@x.com"], [2, "b@x.com"], [4, "c@x.com"]])


def test_single_row():
    person = people((1, "a@x.com"))
    delete_duplicate_emails(person)
    check(person, ["id", "email"], [[1, "a@x.com"]])
