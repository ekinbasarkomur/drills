"""
688. Knight Probability in Chessboard · Medium · https://leetcode.com/problems/knight-probability-in-chessboard/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().knightProbability(3, 2, 0, 0), 0.0625), "close(Solution().knightProbability(3, 2, 0, 0), 0.0625)")


def test_example_2():
    check_true(close(Solution().knightProbability(1, 0, 0, 0), 1.0), "close(Solution().knightProbability(1, 0, 0, 0), 1.0)")
