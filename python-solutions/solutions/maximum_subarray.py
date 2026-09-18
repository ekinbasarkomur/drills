"""
53. Maximum Subarray
 https://leetcode.com/problems/maximum-subarray/

 Problem: the largest sum any contiguous non-empty stretch of nums can
          reach. Every value may be negative.
 Note: At each position you only ever choose between extending the run so
       far and starting fresh -- whichever sum is larger.
 Approach:
 Time O(?), space O(?)
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def max_sub_array(nums: List[int]) -> int:
    return Solution().maxSubArray(nums)


def test_example_1():
    assert max_sub_array([2, -3, 4, -2, 2, 1, -1, 4]) == 8


def test_example_2():
    # the subarray must be non-empty, so 0 is not an answer
    assert max_sub_array([-1]) == -1


def test_single_positive():
    assert max_sub_array([1]) == 1


def test_single_zero():
    assert max_sub_array([0]) == 0


def test_the_classic_leetcode_case():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6


def test_every_value_negative():
    # take the least bad one
    assert max_sub_array([-1, -2, -3]) == -1


def test_a_dip_worth_crossing():
    assert max_sub_array([5, 4, -1, 7, 8]) == 23


def test_alternating_signs():
    assert max_sub_array([1, -1, 1, -1, 1]) == 1


def test_value_range_low():
    assert max_sub_array([-10000]) == -10000


def test_value_range_high():
    assert max_sub_array([10000]) == 10000


def test_largest_allowed_input():
    # 100_000 values alternating +10_000 and -9_999, so each pair nets +1
    # and the best subarray is the whole array.
    # An O(n^2) solution will hang here rather than fail.
    nums = [10_000 if i % 2 == 0 else -9_999 for i in range(100_000)]
    assert max_sub_array(nums) == 59999


if __name__ == "__main__":
    print(max_sub_array([2, -3, 4, -2, 2, 1, -1, 4]))
