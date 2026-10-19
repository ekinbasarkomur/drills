"""
1244. Design A Leaderboard · Medium · https://leetcode.com/problems/design-a-leaderboard/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Leaderboard:

    def __init__(self):
        raise NotImplementedError
    def addScore(self, playerId: int, score: int) -> None:
        raise NotImplementedError
    def top(self, K: int) -> int:
        raise NotImplementedError
    def reset(self, playerId: int) -> None:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    obj = Leaderboard()
    obj.addScore(1, 73)
    obj.addScore(2, 56)
    obj.addScore(3, 39)
    obj.addScore(4, 51)
    obj.addScore(5, 4)
    obj.top(1)
    obj.reset(1)
    obj.reset(2)
    obj.addScore(2, 51)
    obj.top(3)
