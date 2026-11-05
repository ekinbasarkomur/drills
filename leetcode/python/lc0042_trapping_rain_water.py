"""
42. Trapping Rain Water      https://leetcode.com/problems/trapping-rain-water/
Plan: Aşama 0 · Two Pointers

Problem: each height[i] is a bar of width 1. How much water sits in the dips
         once the rain stops?
Key idea: water above bar i is min(tallest bar to its left,
          tallest bar to its right) - height[i], never negative.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def trap(height: list[int]) -> int:
    return Solution().trap(height)


def test_example_1():
    check(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]), 9, "trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1])")


def test_the_leetcode_example():
    check(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6, "trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])")


def test_tall_wall_on_the_right():
    check(trap([4, 2, 0, 3, 2, 5]), 9, "trap([4, 2, 0, 3, 2, 5])")


# Nothing can be trapped in any of these.


def test_single_bar():
    check(trap([5]), 0, "trap([5])")


def test_two_bars():
    check(trap([3, 4]), 0, "trap([3, 4])")


def test_strictly_ascending():
    check(trap([1, 2, 3, 4, 5]), 0, "trap([1, 2, 3, 4, 5])")


def test_strictly_descending():
    check(trap([5, 4, 3, 2, 1]), 0, "trap([5, 4, 3, 2, 1])")


def test_flat_ground():
    check(trap([3, 3, 3, 3]), 0, "trap([3, 3, 3, 3])")


def test_all_zeros():
    check(trap([0, 0, 0]), 0, "trap([0, 0, 0])")


def test_a_peak_traps_nothing():
    check(trap([0, 100_000, 0]), 0, "trap([0, 100_000, 0])")


# The real cases.


def test_one_simple_basin():
    check(trap([5, 0, 5]), 5, "trap([5, 0, 5])")


def test_two_basins_in_a_row():
    check(trap([2, 0, 2, 0, 2]), 4, "trap([2, 0, 2, 0, 2])")


def test_several_narrow_dips():
    check(trap([1, 0, 1, 0, 1, 0, 1]), 3, "trap([1, 0, 1, 0, 1, 0, 1])")


def test_value_range_extremes():
    check(trap([100_000, 0, 100_000]), 100_000, "trap([100_000, 0, 100_000])")


def test_largest_allowed_input():
    # 20_000 bars alternating 100_000 and 0: 9_999 basins of 100_000 each.
    # An O(n^2) solution will hang here rather than fail.
    height = [100_000, 0] * 10_000
    check(trap(height), 999_900_000, "trap(height)")


if __name__ == "__main__":
    print(trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]))
