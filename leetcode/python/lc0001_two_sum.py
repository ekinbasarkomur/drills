"""
1. Two Sum                   https://leetcode.com/problems/two-sum/
Plan: Aşama 0 · Arrays & Hashing

Problem: return the two indices whose values add up to target, smaller first.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in range(0, len(nums)):
            if target - nums[i] in seen:
                return [i, seen[target - nums[i]]]

            seen[nums[i]] = i

        return []
# ---------------------------------------------------------------- tests

# The tests below call the old free functions; forward them to Solution.
# LeetCode accepts the two indices in either order, so compare them sorted.
def two_sum(*args): return sorted(Solution().twoSum(*args))  # noqa: E704


def test_example_1():
    assert two_sum([3, 4, 5, 6], 7) == [0, 1]


def test_example_2():
    assert two_sum([4, 5, 6], 10) == [0, 2]


def test_example_3():
    assert two_sum([5, 5], 10) == [0, 1]


def test_answer_is_the_last_two():
    assert two_sum([1, 9, 3, 4], 7) == [2, 3]


def test_negative_numbers():
    assert two_sum([-3, 4, 7, -1], -4) == [0, 3]


def test_target_is_zero():
    assert two_sum([-8, 2, 8], 0) == [0, 2]


def test_extreme_values():
    assert two_sum([10_000_000, -10_000_000, 3], 0) == [0, 1]


if __name__ == "__main__":
    print(two_sum([3, 4, 5, 6], 7))
