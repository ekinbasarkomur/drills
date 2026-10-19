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
    assert Solution().numberOfSubstrings('abcabc') == 10


def test_example_2():
    assert Solution().numberOfSubstrings('aaacb') == 3


def test_example_3():
    assert Solution().numberOfSubstrings('abc') == 1
