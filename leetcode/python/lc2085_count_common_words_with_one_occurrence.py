"""
2085. Count Common Words With One Occurrence · Easy · https://leetcode.com/problems/count-common-words-with-one-occurrence/
Plan: Aşama 5 · Simülasyon ve Ayrıştırma

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().countWords(['leetcode', 'is', 'amazing', 'as', 'is'], ['amazing', 'leetcode', 'is']) == 2


def test_example_2():
    assert Solution().countWords(['b', 'bb', 'bbb'], ['a', 'aa', 'aaa']) == 0


def test_example_3():
    assert Solution().countWords(['a', 'ab'], ['a', 'a', 'a', 'ab']) == 1
