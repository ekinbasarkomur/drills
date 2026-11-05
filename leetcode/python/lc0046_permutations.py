"""
46. Permutations · Medium · https://leetcode.com/problems/permutations/
Plan: Aşama 4 · Backtracking

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(sorted(Solution().permute([1, 2, 3])), sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]), "sorted(Solution().permute([1, 2, 3]))")


def test_example_2():
    check(sorted(Solution().permute([0, 1])), sorted([[0, 1], [1, 0]]), "sorted(Solution().permute([0, 1]))")


def test_example_3():
    check(sorted(Solution().permute([1])), sorted([[1]]), "sorted(Solution().permute([1]))")
