"""
242. Valid Anagram           https://leetcode.com/problems/valid-anagram/
Plan: Aşama 0 · Arrays & Hashing

Problem: return True if t is a rearrangement of s.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        for index, s_char in enumerate(s):
            t_char = t[index]

            s_map[s_char] = s_map.get(s_char, 0) + 1
            t_map[t_char] = t_map.get(t_char, 0) + 1

        print(s_map)
        print(t_map)

        return s_map == t_map


# ---------------------------------------------------------------- tests

# The tests below call the old free functions; forward them to Solution.
def is_anagram(*args): return Solution().isAnagram(*args)  # noqa: E704


def test_example_1():
    check(is_anagram("racecar", "carrace"), True, 'is_anagram("racecar", "carrace")', op="is")


def test_example_2():
    check(is_anagram("jar", "jam"), False, 'is_anagram("jar", "jam")', op="is")


def test_example_3():
    check(is_anagram("x", "x"), True, 'is_anagram("x", "x")', op="is")


def test_different_lengths():
    check(is_anagram("ab", "abc"), False, 'is_anagram("ab", "abc")', op="is")


def test_same_letters_different_counts():
    check(is_anagram("aab", "abb"), False, 'is_anagram("aab", "abb")', op="is")


def test_identical_strings():
    check(is_anagram("anagram", "anagram"), True, 'is_anagram("anagram", "anagram")', op="is")


def test_no_letters_in_common():
    check(is_anagram("abc", "xyz"), False, 'is_anagram("abc", "xyz")', op="is")


if __name__ == "__main__":
    print(is_anagram("racecar", "carrace"))
