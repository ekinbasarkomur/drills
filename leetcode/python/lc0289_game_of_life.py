"""
289. Game of Life · Medium · https://leetcode.com/problems/game-of-life/
Plan: Aşama 5 · Simülasyon ve Ayrıştırma

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    Solution().gameOfLife(board)
    check(board, [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]], "board")


def test_example_2():
    board = [[1, 1], [1, 0]]
    Solution().gameOfLife(board)
    check(board, [[1, 1], [1, 1]], "board")
