"""
11. Container With Most Water
https://leetcode.com/problems/container-with-most-water/
Plan: Aşama 0 · Two Pointers

Problem: pick two bars; the container they form holds
         (distance between them) * (the shorter of the two). Return the most
         water any pair can hold.
Note: The taller bar never sets the height -- the shorter one does, so a
      wide pair of short bars can beat a narrow pair of tall ones.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def max_area(height: List[int]) -> int:
    return Solution().maxArea(height)


def test_example_1():
    assert max_area([1, 7, 2, 5, 4, 7, 3, 6]) == 36


def test_example_2():
    assert max_area([2, 2, 2]) == 4


def test_shortest_possible_input():
    assert max_area([1, 1]) == 1


def test_two_zero_bars_hold_nothing():
    assert max_area([0, 0]) == 0


def test_the_classic_leetcode_case():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_wide_beats_tall():
    # the two 3s are 2 apart; nothing taller sits closer together
    assert max_area([3, 0, 3]) == 6


def test_strictly_ascending():
    assert max_area([1, 2, 3, 4, 5]) == 6


def test_strictly_descending():
    assert max_area([5, 4, 3, 2, 1]) == 6


def test_one_zero_bar_kills_the_pair():
    assert max_area([0, 10000]) == 0


def test_value_range_extremes():
    assert max_area([10000, 0, 0, 0, 10000]) == 40000


def test_largest_allowed_input():
    # 100_000 bars: 1 at both ends, 0 in between. The answer is the pair of
    # ends, worth 99_999. An O(n^2) solution will hang here rather than fail.
    height = [0] * 100_000
    height[0] = 1
    height[99_999] = 1
    assert max_area(height) == 99999


if __name__ == "__main__":
    print(max_area([1, 7, 2, 5, 4, 7, 3, 6]))
