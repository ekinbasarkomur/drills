"""
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Problem: add() appends to the stream and returns the kth largest value seen so
         far. Duplicates count separately: the 2nd largest of [1,2,3,3] is 3.
Note: you never need the whole stream -- only the k largest values, and of
      those only the smallest is ever the answer.
Approach:
Time O(?) per add, space O(?)
"""

from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        raise NotImplementedError

    def add(self, val: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_example_1():
    s = KthLargest(3, [1, 2, 3, 3])
    assert s.add(3) == 3
    assert s.add(5) == 3
    assert s.add(6) == 3
    assert s.add(7) == 5
    assert s.add(8) == 6


def test_k_is_one_means_the_running_maximum():
    s = KthLargest(1, [])
    assert s.add(5) == 5
    assert s.add(3) == 5
    assert s.add(9) == 9


def test_stream_starts_empty():
    s = KthLargest(2, [])
    s.add(1)
    assert s.add(2) == 1
    assert s.add(3) == 2


def test_initial_array_already_holds_k_values():
    s = KthLargest(3, [4, 5, 8, 2])
    assert s.add(3) == 4
    assert s.add(5) == 5
    assert s.add(10) == 5
    assert s.add(9) == 8


def test_duplicates_count_separately():
    s = KthLargest(2, [3, 3])
    assert s.add(3) == 3
    assert s.add(4) == 3


def test_everything_added_is_smaller():
    s = KthLargest(2, [10, 20, 30])
    assert s.add(1) == 20
    assert s.add(2) == 20


def test_negative_values():
    s = KthLargest(2, [-5, -3, -1])
    assert s.add(-4) == -3
    assert s.add(0) == -1


def test_all_values_equal():
    s = KthLargest(3, [7, 7, 7])
    assert s.add(7) == 7
    assert s.add(8) == 7


def test_value_range_extremes():
    s = KthLargest(2, [-1000, 1000])
    assert s.add(0) == 0
    assert s.add(1000) == 1000


def test_k_equals_the_stream_length():
    s = KthLargest(3, [1, 2])
    assert s.add(3) == 1
    assert s.add(4) == 2


def test_many_operations():
    # 1000 values in, k = 1000: the answer is the running minimum
    # once the stream is long enough.
    s = KthLargest(1000, [])
    last = 0
    for i in range(1000, 0, -1):
        last = s.add(i)
    assert last == 1
