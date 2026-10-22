"""
207. Course Schedule · Medium · https://leetcode.com/problems/course-schedule/
Plan: Aşama 0 · Graphs

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().canFinish(2, [[1, 0]]) == True


def test_example_2():
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) == False
