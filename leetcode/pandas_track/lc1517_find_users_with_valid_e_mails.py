"""
1517. Find Users With Valid E-Mails · Easy · https://leetcode.com/problems/find-users-with-valid-e-mails/
Plan: 30 Days of Pandas · Gün 8 · String Methods

Problem: keep the users whose mail has a valid prefix (starts with a letter; letters, digits, '_', '.', '-') and the domain '@leetcode.com'.
Approach: mail.str.match(regex) gives a boolean mask; where() writes None on the invalid rows and dropna() removes them. ^ and $ anchor the whole string
Time O(n·L), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r"^[A-Za-z][A-Za-z0-9_.\-]*@leetcode\.com$"
    users["mail"] = users["mail"].where(
        cond=users["mail"].str.match(pattern), other=None
    )
    return users.dropna(subset=["mail"])


# ---------------------------------------------------------------- tests


def test_example_1():
    users = frame(
        ["user_id", "name", "mail"],
        [
            [1, "Winston", "winston@leetcode.com"],
            [2, "Jonathan", "jonathanisgreat"],
            [3, "Annabelle", "bella-@leetcode.com"],
            [4, "Sally", "sally.come@leetcode.com"],
            [5, "Marwan", "quarz#2020@leetcode.com"],
            [6, "David", "david69@gmail.com"],
            [7, "Shapiro", ".shapo@leetcode.com"],
        ],
        {"user_id": "int64", "name": "object", "mail": "object"},
    )
    check(
        valid_emails(users),
        ["user_id", "name", "mail"],
        [
            [1, "Winston", "winston@leetcode.com"],
            [3, "Annabelle", "bella-@leetcode.com"],
            [4, "Sally", "sally.come@leetcode.com"],
        ],
        ordered=False,
    )
