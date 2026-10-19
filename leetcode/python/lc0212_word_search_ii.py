"""
212. Word Search II · Hard · https://leetcode.com/problems/word-search-ii/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().findWords([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain']) == ['eat', 'oath']


def test_example_2():
    assert Solution().findWords([['a', 'b'], ['c', 'd']], ['abcb']) == []
