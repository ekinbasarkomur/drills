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
    check(Solution().minDistance('horse', 'ros'), 3, "Solution().minDistance('horse', 'ros')")


def test_example_2():
    check(Solution().minDistance('intention', 'execution'), 5, "Solution().minDistance('intention', 'execution')")
