"""
54. Spiral Matrix · Medium · https://leetcode.com/problems/spiral-matrix/
Plan: Aşama 0 · Matrix

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), [1, 2, 3, 6, 9, 8, 7, 4, 5], "Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])")


def test_example_2():
    check(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7], "Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])")
