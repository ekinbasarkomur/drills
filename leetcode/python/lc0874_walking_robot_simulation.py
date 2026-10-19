"""
874. Walking Robot Simulation · Medium · https://leetcode.com/problems/walking-robot-simulation/
Plan: Aşama 5 · Simülasyon ve Ayrıştırma

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().robotSim([4, -1, 3], []) == 25


def test_example_2():
    assert Solution().robotSim([4, -1, 4, -2, 4], [[2, 4]]) == 65


def test_example_3():
    assert Solution().robotSim([-1, 9], [[5, 0], [2, 0]]) == 36
