"""
253. Meeting Rooms II · Medium · https://leetcode.com/problems/meeting-rooms-ii/
Plan: Aşama 2 · Intervals ve Sweep Line

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    Solution().minMeetingRooms([[0, 30], [5, 10], [15, 20]])


def test_example_2():
    # Premium problem: the expected output is not public, so this only runs it.
    Solution().minMeetingRooms([[7, 10], [2, 4]])
