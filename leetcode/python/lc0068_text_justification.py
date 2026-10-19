"""
68. Text Justification · Hard · https://leetcode.com/problems/text-justification/
Plan: Aşama 5 · Simülasyon ve Ayrıştırma

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().fullJustify(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16) == ['This    is    an', 'example  of text', 'justification.  ']


def test_example_2():
    assert Solution().fullJustify(['What', 'must', 'be', 'acknowledgment', 'shall', 'be'], 16) == ['What   must   be', 'acknowledgment  ', 'shall be        ']


def test_example_3():
    assert Solution().fullJustify(['Science', 'is', 'what', 'we', 'understand', 'well', 'enough', 'to', 'explain', 'to', 'a', 'computer.', 'Art', 'is', 'everything', 'else', 'we', 'do'], 20) == ['Science  is  what we', 'understand      well', 'enough to explain to', 'a  computer.  Art is', 'everything  else  we', 'do                  ']
