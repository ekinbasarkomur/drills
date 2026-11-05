"""
17. Letter Combinations of a Phone Number · Medium · https://leetcode.com/problems/letter-combinations-of-a-phone-number/
Plan: Aşama 4 · Backtracking

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(deep_sorted(Solution().letterCombinations('23')), deep_sorted(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']), "deep_sorted(Solution().letterCombinations('23'))")


def test_example_2():
    check(deep_sorted(Solution().letterCombinations('2')), deep_sorted(['a', 'b', 'c']), "deep_sorted(Solution().letterCombinations('2'))")
