"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
Plan: Aşama 0 · Sliding Window

Problem: after replacing at most k characters of s with any uppercase
         letter, how long can a run of one single letter get?
Note: A window is usable when (its length - the count of its most common
      letter) <= k: that difference is how many replacements it costs.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
from typing import List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def character_replacement(s: str, k: int) -> int:
    return Solution().characterReplacement(s, k)


def test_example_1():
    # replace both X's with Y's, or the other way round
    check(character_replacement("XYYX", 2), 4, 'character_replacement("XYYX", 2)')


def test_example_2():
    check(character_replacement("AAABABB", 1), 5, 'character_replacement("AAABABB", 1)')


def test_single_character_no_budget():
    check(character_replacement("A", 0), 1, 'character_replacement("A", 0)')


def test_single_character_with_budget():
    # k can exceed what is useful
    check(character_replacement("A", 1), 1, 'character_replacement("A", 1)')


def test_two_letters_no_budget():
    check(character_replacement("AB", 0), 1, 'character_replacement("AB", 0)')


def test_two_letters_one_replacement():
    check(character_replacement("AB", 1), 2, 'character_replacement("AB", 1)')


def test_already_uniform():
    # nothing to replace
    check(character_replacement("BBBB", 0), 4, 'character_replacement("BBBB", 0)')


def test_all_distinct_no_budget():
    check(character_replacement("ABCDE", 0), 1, 'character_replacement("ABCDE", 0)')


def test_all_distinct_budget_covers_everything():
    check(character_replacement("ABCDE", 4), 5, 'character_replacement("ABCDE", 4)')


def test_budget_larger_than_needed():
    check(character_replacement("AAAA", 2), 4, 'character_replacement("AAAA", 2)')


def test_one_odd_letter_at_the_front():
    check(character_replacement("ABBB", 0), 3, 'character_replacement("ABBB", 0)')


def test_the_window_must_shrink():
    check(character_replacement("AABABBA", 1), 4, 'character_replacement("AABABBA", 1)')


def test_alternating_letters():
    check(character_replacement("ABAB", 2), 4, 'character_replacement("ABAB", 2)')


def test_largest_allowed_input():
    # 100_000 A's and k = 0: the whole string already qualifies.
    # An O(n^2) solution will hang here rather than fail.
    s = "A" * 100_000
    check(character_replacement(s, 0), 100000, "character_replacement(s, 0)")


if __name__ == "__main__":
    print(character_replacement("XYYX", 2))
