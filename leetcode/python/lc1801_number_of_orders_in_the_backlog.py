"""
1801. Number of Orders in the Backlog · Medium · https://leetcode.com/problems/number-of-orders-in-the-backlog/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]), 6, "Solution().getNumberOfBacklogOrders([[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]])")


def test_example_2():
    check(Solution().getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]]), 999999984, "Solution().getNumberOfBacklogOrders([[7, 1000000000, 1], [15, 3, 0], [5, 999999995, 0], [5, 1, 1]])")
