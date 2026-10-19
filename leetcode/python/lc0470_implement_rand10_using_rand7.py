"""
470. Implement Rand10() Using Rand7() · Medium · https://leetcode.com/problems/implement-rand10-using-rand7/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)


def rand7():  # LeetCode provides it; this one stands in
    return random.randint(1, 7)


# ---------------------------------------------------------------- solution
# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        raise NotImplementedError


# ---------------------------------------------------------------- tests

# No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
# Write your own below if you want a local check.
