"""
3. Longest Substring Without Repeating Characters
 https://leetcode.com/problems/longest-substring-without-repeating-characters/

 Problem: length of the longest contiguous stretch of s in which no
          character repeats. s may contain any printable ASCII.
 Note: A window that only ever grows from the right and shrinks from the
       left visits each character twice at most.
 Approach:
 Time O(?), space O(?)
"""

from typing import List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def length_of_longest_substring(s: str) -> int:
    return Solution().lengthOfLongestSubstring(s)


def test_example_1():
    assert length_of_longest_substring("zxyzxyz") == 3


def test_example_2():
    assert length_of_longest_substring("xxxx") == 1


def test_empty_string():
    assert length_of_longest_substring("") == 0


def test_single_character():
    assert length_of_longest_substring("a") == 1


def test_two_distinct_characters():
    assert length_of_longest_substring("ab") == 2


def test_every_character_is_the_same():
    assert length_of_longest_substring("bbbbb") == 1


def test_the_classic_leetcode_case():
    assert length_of_longest_substring("abcabcbb") == 3


def test_the_answer_is_not_a_prefix():
    # \"wke\", not \"pwe\" -- the answer must be contiguous
    assert length_of_longest_substring("pwwkew") == 3


def test_a_repeat_before_the_window_start():
    # after 'a' repeats the window must not jump back behind the second 'b'
    assert length_of_longest_substring("abba") == 2


def test_stale_index_must_be_ignored():
    # \"mzuxt\"
    assert length_of_longest_substring("tmmzuxt") == 5


def test_spaces_count_as_characters():
    assert length_of_longest_substring("a b c") == 3


def test_punctuation_and_symbols():
    assert length_of_longest_substring(" !@# !@#") == 4


def test_largest_allowed_input():
    # 50_000 characters cycling through the 95 printable ASCII codes, so the
    # answer is one full cycle. An O(n^2) solution will hang here.
    s = "".join(chr(32 + i % 95) for i in range(50_000))
    assert length_of_longest_substring(s) == 95


if __name__ == "__main__":
    print(length_of_longest_substring("zxyzxyz"))
