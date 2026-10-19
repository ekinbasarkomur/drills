"""
210. Course Schedule II · Medium · https://leetcode.com/problems/course-schedule-ii/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().findOrder(2, [[1, 0]]) == [0, 1]


def test_example_2():
    assert Solution().findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]) == [0, 2, 1, 3]


def test_example_3():
    assert Solution().findOrder(1, []) == [0]
