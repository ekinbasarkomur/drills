"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/
Plan: Aşama 0 · Stack

Problem: every bracket closed by its own kind, in the right order,
         and nothing left open at the end.
Note: The most recently opened bracket is the first that has to close --
      that is exactly what a stack gives you.
Approach: the open_close dict gives the closer each opener expects and it is pushed;
          on a closer, pop and compare. A closer on an empty stack is invalid; valid if nothing is left.
Time O(n), space O(n)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def isValid(self, s: str) -> bool:
        expected = []
        open_close={"(":")","{":"}","[":"]"}

        for c in s:
            if len(expected) == 0:
                if c in [')', '}', ']']:
                    return False 
            
            if c in ['(', '{', '[']:
                expected.append(open_close[c])
            elif expected.pop() != c:
                return False               


        return len(expected) == 0
# ---------------------------------------------------------------- tests


def is_valid(s: str) -> bool:
    return Solution().isValid(s)


def test_example_1():
    check(is_valid("[]"), True, 'is_valid("[]")')


def test_example_2():
    check(is_valid("([{}])"), True, 'is_valid("([{}])")')


def test_example_3():
    # right counts, wrong order
    check(is_valid("[(])"), False, 'is_valid("[(])")')


def test_empty_string():
    # nothing left open
    check(is_valid(""), True, 'is_valid("")')


def test_one_opening_bracket():
    check(is_valid("("), False, 'is_valid("(")')


def test_one_closing_bracket():
    check(is_valid(")"), False, 'is_valid(")")')


def test_all_three_kinds_side_by_side():
    check(is_valid("()[]{}"), True, 'is_valid("()[]{}")')


def test_mismatched_pair():
    check(is_valid("(]"), False, 'is_valid("(]")')


def test_a_wrong_closer_is_not_skipped():
    # the ']' must fail immediately; ignoring it lets ')' close the '('
    check(is_valid("(])"), False, 'is_valid("(])")')


def test_only_openers():
    check(is_valid("(((("), False, 'is_valid("((((")')


def test_only_closers():
    check(is_valid("))))"), False, 'is_valid("))))")')


def test_deeply_nested():
    check(is_valid("{[()]}"), True, 'is_valid("{[()]}")')


def test_one_opener_left_over():
    check(is_valid("(()"), False, 'is_valid("(()")')


def test_one_closer_too_many():
    check(is_valid("())"), False, 'is_valid("())")')


def test_largest_allowed_input():
    # 1000 brackets: 500 openers then 500 closers, the constraint's ceiling.
    s = "(" * 500 + ")" * 500
    check(is_valid(s), True, "is_valid(s)")


if __name__ == "__main__":
    print(is_valid("[]"))
