"""
73. Set Matrix Zeroes · Medium · https://leetcode.com/problems/set-matrix-zeroes/
Plan: Aşama 0 · Matrix

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    check(matrix, [[1, 0, 1], [0, 0, 0], [1, 0, 1]], "matrix")


def test_example_2():
    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    Solution().setZeroes(matrix)
    check(matrix, [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]], "matrix")
