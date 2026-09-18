"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Problem: nums was sorted ascending, then rotated some number of times.
         Return the index of target, or -1. O(log n) is the point.
Note: At any midpoint one of the two halves is still properly sorted.
      Work out which, and you know whether target can be in it.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def search(nums: List[int], target: int) -> int:
    return Solution().search(nums, target)


def test_example_1():
    assert search([3, 4, 5, 6, 1, 2], 1) == 4


def test_example_2():
    assert search([3, 5, 6, 0, 1, 2], 4) == -1


def test_single_element_found():
    assert search([1], 1) == 0


def test_single_element_missing():
    assert search([1], 2) == -1


def test_not_rotated_at_all():
    # a full rotation looks like no rotation
    assert search([1, 2, 3, 4, 5, 6], 4) == 3


def test_target_is_the_pivot():
    assert search([4, 5, 6, 7, 0, 1, 2], 0) == 4


def test_target_missing_inside_the_range():
    assert search([4, 5, 6, 7, 0, 1, 2], 3) == -1


def test_rotated_by_one():
    assert search([2, 1], 1) == 1


def test_target_is_the_first_element():
    assert search([5, 1, 2, 3, 4], 5) == 0


def test_negative_values():
    assert search([0, 1, 2, -3, -2, -1], -3) == 3


def test_largest_allowed_input():
    # 1000 elements rotated so the smallest sits in the middle.
    # The answer is at index 0.
    nums = list(range(500, 1_000)) + list(range(500))
    assert search(nums, 500) == 0


if __name__ == "__main__":
    print(search([3, 4, 5, 6, 1, 2], 1))
