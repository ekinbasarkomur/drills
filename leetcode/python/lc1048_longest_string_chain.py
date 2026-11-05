"""
1048. Longest String Chain · Medium · https://leetcode.com/problems/longest-string-chain/
Plan: Aşama 4 · Stock Serisi ve DP

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca']), 4, "Solution().longestStrChain(['a', 'b', 'ba', 'bca', 'bda', 'bdca'])")


def test_example_2():
    check(Solution().longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc']), 5, "Solution().longestStrChain(['xbc', 'pcxbcf', 'xb', 'cxbc', 'pcxbc'])")


def test_example_3():
    check(Solution().longestStrChain(['abcd', 'dbqca']), 1, "Solution().longestStrChain(['abcd', 'dbqca'])")
