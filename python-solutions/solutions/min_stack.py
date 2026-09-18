"""
155. Min Stack
https://leetcode.com/problems/min-stack/

Problem: a stack that also answers getMin() -- all four operations in O(1).
Note: getMin in O(1) is the whole problem. Scanning for the minimum is O(n),
      and a single "current min" variable cannot survive a pop that removes it,
      because you no longer know what the minimum was before.
Approach:
Time O(?) per operation, space O(?)
"""


class MinStack:
    def __init__(self):
        raise NotImplementedError

    def push(self, val: int) -> None:
        raise NotImplementedError

    def pop(self) -> None:
        raise NotImplementedError

    def top(self) -> int:
        raise NotImplementedError

    def getMin(self) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_example_1():
    s = MinStack()
    s.push(1)
    s.push(2)
    s.push(0)
    assert s.getMin() == 0
    s.pop()
    assert s.top() == 2
    assert s.getMin() == 1


def test_single_element():
    s = MinStack()
    s.push(5)
    assert s.top() == 5
    assert s.getMin() == 5


def test_min_is_the_first_pushed():
    s = MinStack()
    for v in (1, 2, 3):
        s.push(v)
    assert s.getMin() == 1
    assert s.top() == 3


def test_min_is_the_last_pushed():
    s = MinStack()
    for v in (3, 2, 1):
        s.push(v)
    assert s.getMin() == 1


def test_popping_the_minimum_restores_the_previous_one():
    s = MinStack()
    s.push(5)
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 5


def test_duplicate_minimums():
    # popping one copy of the minimum must not lose the other
    s = MinStack()
    for v in (2, 1, 1):
        s.push(v)
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 1
    s.pop()
    assert s.getMin() == 2


def test_negative_values():
    s = MinStack()
    for v in (0, -3, 2):
        s.push(v)
    assert s.getMin() == -3
    s.pop()
    assert s.getMin() == -3


def test_emptied_and_refilled():
    s = MinStack()
    s.push(1)
    s.pop()
    s.push(9)
    assert s.top() == 9
    assert s.getMin() == 9


def test_interleaved_operations():
    s = MinStack()
    s.push(4)
    assert s.getMin() == 4
    s.push(7)
    assert s.getMin() == 4
    s.push(2)
    assert s.getMin() == 2
    s.pop()
    assert s.getMin() == 4
    s.push(1)
    assert s.getMin() == 1
    s.pop()
    s.pop()
    assert s.top() == 4
    assert s.getMin() == 4


def test_value_range_extremes():
    s = MinStack()
    s.push(2**31 - 1)
    s.push(-(2**31))
    assert s.getMin() == -(2**31)
    s.pop()
    assert s.getMin() == 2**31 - 1


def test_many_operations_stay_constant_time():
    # 30_000 pushes then 30_000 pops, the constraint's ceiling.
    # An O(n) getMin will crawl here.
    s = MinStack()
    for i in range(30_000, 0, -1):
        s.push(i)
    for i in range(1, 30_001):
        assert s.getMin() == i
        s.pop()
