"""
2050. Parallel Courses III · Hard · https://leetcode.com/problems/parallel-courses-iii/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def minimumTime(self, n: int, relations: list[list[int]], time: list[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5]), 8, "Solution().minimumTime(3, [[1, 3], [2, 3]], [3, 2, 5])")


def test_example_2():
    check(Solution().minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5]), 12, "Solution().minimumTime(5, [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]], [1, 2, 3, 4, 5])")
