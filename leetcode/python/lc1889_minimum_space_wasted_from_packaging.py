"""
1889. Minimum Space Wasted From Packaging · Hard · https://leetcode.com/problems/minimum-space-wasted-from-packaging/
Plan: Aşama 1 · Binary Search

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minWastedSpace(self, packages: list[int], boxes: list[list[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().minWastedSpace([2, 3, 5], [[4, 8], [2, 8]]), 6, "Solution().minWastedSpace([2, 3, 5], [[4, 8], [2, 8]])")


def test_example_2():
    check(Solution().minWastedSpace([2, 3, 5], [[1, 4], [2, 3], [3, 4]]), -1, "Solution().minWastedSpace([2, 3, 5], [[1, 4], [2, 3], [3, 4]])")


def test_example_3():
    check(Solution().minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]]), 9, "Solution().minWastedSpace([3, 5, 8, 10, 11, 12], [[12], [11, 9], [10, 5, 14]])")
