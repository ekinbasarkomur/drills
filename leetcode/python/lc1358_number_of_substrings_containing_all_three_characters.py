"""
1358. Number of Substrings Containing All Three Characters · Medium · https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/
Plan: Aşama 1 · Prefix Sum ve Sliding Window

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().numberOfSubstrings('abcabc'), 10, "Solution().numberOfSubstrings('abcabc')")


def test_example_2():
    check(Solution().numberOfSubstrings('aaacb'), 3, "Solution().numberOfSubstrings('aaacb')")


def test_example_3():
    check(Solution().numberOfSubstrings('abc'), 1, "Solution().numberOfSubstrings('abc')")
