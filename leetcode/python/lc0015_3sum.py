"""
15. 3Sum
https://leetcode.com/problems/3sum/
Plan: Aşama 0 · Two Pointers

Problem: every triplet of distinct indices summing to zero, with no duplicate
         triplets in the output. Order does not matter.
Note: the hard part is not finding the triplets, it is not emitting the same
      one twice -- [-1,0,1] can be built from several index combinations.
Approach:
Time O(?), space O(?)
"""

# ---------------------------------------------------------------- solution
from typing import List

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        sorted_nums = sorted(nums)

        for i in range(0, len(nums) - 2):
            if (i > 0) and (sorted_nums[i] == sorted_nums[i - 1]):
                continue

            target = -sorted_nums[i]

            left = i + 1
            right = len(nums) - 1

            while left < right:
                summed = sorted_nums[left] + sorted_nums[right]

                if summed < target:
                    left += 1

                elif summed > target:
                    right -= 1

                else:
                    output.append(
                        [sorted_nums[i], sorted_nums[left], sorted_nums[right]]
                    )
                    print(output[-1])

                    left += 1
                    right -= 1

                    while left < right and sorted_nums[left] == sorted_nums[left - 1]:
                        left += 1

        return output


# ---------------------------------------------------------------- tests
# "You may return the output and the triplets in any order" -> sort both
# levels before comparing.


def three_sum(nums: list[int]) -> list[list[int]]:
    return sorted(sorted(t) for t in Solution().threeSum(list(nums)))


def expect(triplets: list[list[int]]) -> list[list[int]]:
    return sorted(sorted(t) for t in triplets)


def test_example_1():
    assert three_sum([-1, 0, 1, 2, -1, -4]) == expect([[-1, -1, 2], [-1, 0, 1]])


def test_example_2():
    assert three_sum([0, 1, 1]) == expect([])


def test_example_3():
    assert three_sum([0, 0, 0]) == expect([[0, 0, 0]])


def test_all_positive_cannot_reach_zero():
    assert three_sum([1, 2, 3]) == expect([])


def test_all_negative_cannot_reach_zero():
    assert three_sum([-1, -2, -3]) == expect([])


# Duplicate handling: the same triplet must appear exactly once.


def test_four_zeros_yield_one_triplet():
    assert three_sum([0, 0, 0, 0]) == expect([[0, 0, 0]])


def test_a_repeated_value_inside_a_triplet():
    assert three_sum([-2, 0, 1, 1, 2]) == expect([[-2, 0, 2], [-2, 1, 1]])


def test_many_repeats_many_triplets():
    assert three_sum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]) == expect(
        [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]
    )


def test_same_values_different_order_in_the_input():
    assert three_sum([1, -1, 0, 2, -2, 0]) == expect([[-2, 0, 2], [-1, 0, 1]])


def test_value_range_extremes():
    assert three_sum([100_000, -100_000, 0]) == expect([[-100_000, 0, 100_000]])
    assert three_sum([-100_000, 50_000, 50_000]) == expect([[-100_000, 50_000, 50_000]])


def test_largest_allowed_input():
    # 3000 elements, all 1 except three that form the only triplet.
    # An O(n^3) solution will hang here rather than fail.
    nums = [1] * 2997 + [-5, 2, 3]
    assert three_sum(nums) == expect([[-5, 2, 3]])


if __name__ == "__main__":
    print(three_sum([-1, 0, 1, 2, -1, -4]))
