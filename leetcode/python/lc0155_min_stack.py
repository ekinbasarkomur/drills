"""
155. Min Stack
https://leetcode.com/problems/min-stack/
Plan: Aşama 0 · Stack

Problem: a stack that also answers getMin() -- all four operations in O(1).
Note: getMin in O(1) is the whole problem. Scanning for the minimum is O(n),
      and a single "current min" variable cannot survive a pop that removes it,
      because you no longer know what the minimum was before.
Approach: a second stack records, for every element pushed, the minimum at
          that moment. Popping both keeps them in step, so the previous
          minimum is always sitting underneath -- nothing to recompute.
Time O(1) per operation, space O(n)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack:
            self.min_stack.append(min(val, self.min_stack[-1]))
        else:
            self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# ---------------------------------------------------------------- tests


def test_example_1():
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    check(s.getMin(), 0, "s.getMin()")
    s.pop()
    check(s.top(), 2, "s.top()")
    check(s.getMin(), 1, "s.getMin()")


def test_single_element():
    s = MinStack()
    s.push(5)
    check(s.top(), 5, "s.top()")
    check(s.getMin(), 5, "s.getMin()")


def test_min_is_the_first_pushed():
    s = MinStack()
    for v in (1, 2, 3):
        s.push(v)
    check(s.getMin(), 1, "s.getMin()")
    check(s.top(), 3, "s.top()")


def test_min_is_the_last_pushed():
    s = MinStack()
    for v in (3, 2, 1):
        s.push(v)
    check(s.getMin(), 1, "s.getMin()")


def test_popping_the_minimum_restores_the_previous_one():
    s = MinStack()
    s.push(5)
    s.push(1)
    check(s.getMin(), 1, "s.getMin()")
    s.pop()
    check(s.getMin(), 5, "s.getMin()")


def test_duplicate_minimums():
    # popping one copy of the minimum must not lose the other
    s = MinStack()
    for v in (2, 1, 1):
        s.push(v)
    check(s.getMin(), 1, "s.getMin()")
    s.pop()
    check(s.getMin(), 1, "s.getMin()")
    s.pop()
    check(s.getMin(), 2, "s.getMin()")


def test_negative_values():
    s = MinStack()
    for v in (0, -3, 2):
        s.push(v)
    check(s.getMin(), -3, "s.getMin()")
    s.pop()
    check(s.getMin(), -3, "s.getMin()")


def test_emptied_and_refilled():
    s = MinStack()
    s.push(1)
    s.pop()
    s.push(9)
    check(s.top(), 9, "s.top()")
    check(s.getMin(), 9, "s.getMin()")


def test_interleaved_operations():
    s = MinStack()
    s.push(4)
    check(s.getMin(), 4, "s.getMin()")
    s.push(7)
    check(s.getMin(), 4, "s.getMin()")
    s.push(2)
    check(s.getMin(), 2, "s.getMin()")
    s.pop()
    check(s.getMin(), 4, "s.getMin()")
    s.push(1)
    check(s.getMin(), 1, "s.getMin()")
    s.pop()
    s.pop()
    check(s.top(), 4, "s.top()")
    check(s.getMin(), 4, "s.getMin()")


def test_value_range_extremes():
    s = MinStack()
    s.push(2**31 - 1)
    s.push(-(2**31))
    check(s.getMin(), -(2**31), "s.getMin()")
    s.pop()
    check(s.getMin(), 2**31 - 1, "s.getMin()")


def test_many_operations_stay_constant_time():
    # 30_000 pushes then 30_000 pops, the constraint's ceiling.
    # An O(n) getMin will crawl here.
    s = MinStack()
    for i in range(30_000, 0, -1):
        s.push(i)
    for i in range(1, 30_001):
        check(s.getMin(), i, "s.getMin()")
        s.pop()
