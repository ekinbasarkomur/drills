"""
767. Reorganize String · Medium · https://leetcode.com/problems/reorganize-string/
Plan: Aşama 2 · Data Stream ve Heap

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def reorganizeString(self, s: str) -> str:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().reorganizeString('aab'), 'aba', "Solution().reorganizeString('aab')")


def test_example_2():
    check(Solution().reorganizeString('aaab'), '', "Solution().reorganizeString('aaab')")
