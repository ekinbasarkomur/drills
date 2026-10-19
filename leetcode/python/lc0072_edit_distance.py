"""
72. Edit Distance · Medium · https://leetcode.com/problems/edit-distance/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().minDistance('horse', 'ros') == 3


def test_example_2():
    assert Solution().minDistance('intention', 'execution') == 5
