"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
Plan: Aşama 0 · Sliding Window

Problem: length of the longest contiguous stretch of s in which no
         character repeats. s may contain any printable ASCII.
Note: A window that only ever grows from the right and shrinks from the
      left visits each character twice at most.
Approach: sliding window with a last-seen index per character. `right` adds one
          character per step; if that character was last seen inside the window,
          `left` jumps straight past that position (no inner loop).
Time O(n), space O(min(n, 95))
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        longest_streak = 0
        left = 0

        for right, c in enumerate(s):
            if c in last and last[c] >= left:
                left = last[c] + 1
            
            last[c] = right
            longest_streak = max(longest_streak, right - left + 1)

        return longest_streak
# ---------------------------------------------------------------- tests


def length_of_longest_substring(s: str) -> int:
    return Solution().lengthOfLongestSubstring(s)


def test_example_1():
    check(length_of_longest_substring("zxyzxyz"), 3, 'length_of_longest_substring("zxyzxyz")')


def test_example_2():
    check(length_of_longest_substring("xxxx"), 1, 'length_of_longest_substring("xxxx")')


def test_empty_string():
    check(length_of_longest_substring(""), 0, 'length_of_longest_substring("")')


def test_single_character():
    check(length_of_longest_substring("a"), 1, 'length_of_longest_substring("a")')


def test_two_distinct_characters():
    check(length_of_longest_substring("ab"), 2, 'length_of_longest_substring("ab")')


def test_every_character_is_the_same():
    check(length_of_longest_substring("bbbbb"), 1, 'length_of_longest_substring("bbbbb")')


def test_the_classic_leetcode_case():
    check(length_of_longest_substring("abcabcbb"), 3, 'length_of_longest_substring("abcabcbb")')


def test_the_answer_is_not_a_prefix():
    # \"wke\", not \"pwe\" -- the answer must be contiguous
    check(length_of_longest_substring("pwwkew"), 3, 'length_of_longest_substring("pwwkew")')


def test_a_repeat_before_the_window_start():
    # after 'a' repeats the window must not jump back behind the second 'b'
    check(length_of_longest_substring("abba"), 2, 'length_of_longest_substring("abba")')


def test_stale_index_must_be_ignored():
    # \"mzuxt\"
    check(length_of_longest_substring("tmmzuxt"), 5, 'length_of_longest_substring("tmmzuxt")')


def test_a_repeat_keeps_the_characters_after_it():
    # at the second 'a' the window becomes "bca", not "a"
    check(length_of_longest_substring("abcad"), 4, 'length_of_longest_substring("abcad")')


def test_the_answer_spans_the_repeated_character():
    # "vdf": the second 'd' only evicts the first 'd', 'v' stays
    check(length_of_longest_substring("dvdf"), 3, 'length_of_longest_substring("dvdf")')


def test_spaces_count_as_characters():
    check(length_of_longest_substring("a b c"), 3, 'length_of_longest_substring("a b c")')


def test_punctuation_and_symbols():
    check(length_of_longest_substring(" !@# !@#"), 4, 'length_of_longest_substring(" !@# !@#")')


def test_largest_allowed_input():
    # 50_000 characters cycling through the 95 printable ASCII codes, so the
    # answer is one full cycle. An O(n^2) solution will hang here.
    s = "".join(chr(32 + i % 95) for i in range(50_000))
    check(length_of_longest_substring(s), 95, "length_of_longest_substring(s)")


if __name__ == "__main__":
    print(length_of_longest_substring("zxyzxyz"))
