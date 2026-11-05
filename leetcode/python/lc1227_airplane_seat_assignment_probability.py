"""
1227. Airplane Seat Assignment Probability · Medium · https://leetcode.com/problems/airplane-seat-assignment-probability/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def nthPersonGetsNthSeat(self, n: int) -> float:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().nthPersonGetsNthSeat(1), 1.0), "close(Solution().nthPersonGetsNthSeat(1), 1.0)")


def test_example_2():
    check_true(close(Solution().nthPersonGetsNthSeat(2), 0.5), "close(Solution().nthPersonGetsNthSeat(2), 0.5)")
