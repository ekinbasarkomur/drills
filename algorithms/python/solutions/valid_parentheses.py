"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Problem: every bracket closed by its own kind, in the right order,
         and nothing left open at the end.
Note: The most recently opened bracket is the first that has to close --
      that is exactly what a stack gives you.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def is_valid(s: str) -> bool:
    return Solution().isValid(s)


def test_example_1():
    assert is_valid("[]") == True


def test_example_2():
    assert is_valid("([{}])") == True


def test_example_3():
    # right counts, wrong order
    assert is_valid("[(])") == False


def test_empty_string():
    # nothing left open
    assert is_valid("") == True


def test_one_opening_bracket():
    assert is_valid("(") == False


def test_one_closing_bracket():
    assert is_valid(")") == False


def test_all_three_kinds_side_by_side():
    assert is_valid("()[]{}") == True


def test_mismatched_pair():
    assert is_valid("(]") == False


def test_a_wrong_closer_is_not_skipped():
    # the ']' must fail immediately; ignoring it lets ')' close the '('
    assert is_valid("(])") == False


def test_only_openers():
    assert is_valid("((((") == False


def test_only_closers():
    assert is_valid("))))") == False


def test_deeply_nested():
    assert is_valid("{[()]}") == True


def test_one_opener_left_over():
    assert is_valid("(()") == False


def test_one_closer_too_many():
    assert is_valid("())") == False


def test_largest_allowed_input():
    # 1000 brackets: 500 openers then 500 closers, the constraint's ceiling.
    s = "(" * 500 + ")" * 500
    assert is_valid(s) == True


if __name__ == "__main__":
    print(is_valid("[]"))
