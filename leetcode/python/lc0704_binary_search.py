"""
704. Binary Search
https://leetcode.com/problems/binary-search/
Plan: Aşama 0 · Binary Search

Problem: nums is sorted ascending and every value is distinct. Return the
         index of target, or -1. Must run in O(log n).
Note: The classic bug is the loop bound: <= vs <, and whether the midpoint
      moves. Get those wrong and it either misses the answer or hangs.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def search(nums: List[int], target: int) -> int:
    return Solution().search(nums, target)


def test_example_1():
    check(search([-1, 0, 2, 4, 6, 8], 4), 3, "search([-1, 0, 2, 4, 6, 8], 4)")


def test_example_2():
    check(search([-1, 0, 2, 4, 6, 8], 3), -1, "search([-1, 0, 2, 4, 6, 8], 3)")


def test_single_element_found():
    check(search([5], 5), 0, "search([5], 5)")


def test_single_element_missing():
    check(search([5], 1), -1, "search([5], 1)")


def test_two_elements_first():
    check(search([1, 2], 1), 0, "search([1, 2], 1)")


def test_two_elements_second():
    check(search([1, 2], 2), 1, "search([1, 2], 2)")


def test_target_at_the_front():
    check(search([1, 3, 5, 7, 9], 1), 0, "search([1, 3, 5, 7, 9], 1)")


def test_target_at_the_back():
    check(search([1, 3, 5, 7, 9], 9), 4, "search([1, 3, 5, 7, 9], 9)")


def test_below_everything():
    check(search([1, 3, 5, 7, 9], 0), -1, "search([1, 3, 5, 7, 9], 0)")


def test_above_everything():
    check(search([1, 3, 5, 7, 9], 10), -1, "search([1, 3, 5, 7, 9], 10)")


def test_negative_values():
    check(search([-9, -7, -3, -1], -7), 1, "search([-9, -7, -3, -1], -7)")


def test_largest_allowed_input():
    # 10_000 elements, the constraint's ceiling, and the answer is the last
    # one. Binary search finds it in 14 steps; a linear scan takes 10_000.
    nums = list(range(10_000))
    check(search(nums, 9_999), 9999, "search(nums, 9_999)")


if __name__ == "__main__":
    print(search([-1, 0, 2, 4, 6, 8], 4))
