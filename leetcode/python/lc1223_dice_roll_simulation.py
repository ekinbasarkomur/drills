"""
1223. Dice Roll Simulation · Hard · https://leetcode.com/problems/dice-roll-simulation/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def dieSimulator(self, n: int, rollMax: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().dieSimulator(2, [1, 1, 2, 2, 2, 3]), 34, "Solution().dieSimulator(2, [1, 1, 2, 2, 2, 3])")


def test_example_2():
    check(Solution().dieSimulator(2, [1, 1, 1, 1, 1, 1]), 30, "Solution().dieSimulator(2, [1, 1, 1, 1, 1, 1])")


def test_example_3():
    check(Solution().dieSimulator(3, [1, 1, 1, 2, 2, 3]), 181, "Solution().dieSimulator(3, [1, 1, 1, 2, 2, 3])")
