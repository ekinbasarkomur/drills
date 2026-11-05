"""
636. Exclusive Time of Functions · Medium · https://leetcode.com/problems/exclusive-time-of-functions/
Plan: Aşama 5 · Simülasyon ve Ayrıştırma

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().exclusiveTime(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6']), [3, 4], "Solution().exclusiveTime(2, ['0:start:0', '1:start:2', '1:end:5', '0:end:6'])")


def test_example_2():
    check(Solution().exclusiveTime(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7']), [8], "Solution().exclusiveTime(1, ['0:start:0', '0:start:2', '0:end:5', '0:start:6', '0:end:6', '0:end:7'])")


def test_example_3():
    check(Solution().exclusiveTime(2, ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7']), [7, 1], "Solution().exclusiveTime(2, ['0:start:0', '0:start:2', '0:end:5', '1:start:6', '1:end:6', '0:end:7'])")
