"""
3161. Block Placement Queries · Hard · https://leetcode.com/problems/block-placement-queries/
Plan: Aşama 5 · Segment Tree ve Fenwick

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]]), [False, True, True], "Solution().getResults([[1, 2], [2, 3, 3], [2, 3, 1], [2, 2, 2]])")


def test_example_2():
    check(Solution().getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]]), [True, True, False], "Solution().getResults([[1, 7], [2, 7, 6], [1, 2], [2, 7, 5], [2, 7, 6]])")
