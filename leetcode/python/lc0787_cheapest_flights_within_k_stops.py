"""
787. Cheapest Flights Within K Stops · Medium · https://leetcode.com/problems/cheapest-flights-within-k-stops/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1), 700, "Solution().findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1)")


def test_example_2():
    check(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1), 200, "Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1)")


def test_example_3():
    check(Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0), 500, "Solution().findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0)")
