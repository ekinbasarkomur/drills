"""
743. Network Delay Time · Medium · https://leetcode.com/problems/network-delay-time/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2) == 2


def test_example_2():
    assert Solution().networkDelayTime([[1, 2, 1]], 2, 1) == 1


def test_example_3():
    assert Solution().networkDelayTime([[1, 2, 1]], 2, 2) == -1
