"""
125. Valid Palindrome        https://leetcode.com/problems/valid-palindrome/
Plan: Aşama 0 · Two Pointers

Problem: is s a palindrome, ignoring case and every non-alphanumeric character?
Approach: filter the string down to lowercased alphanumerics, then compare the
          first half against the last half walking inwards from both ends.
          Time O(n), space O(n).
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def isPalindrome(self, s: str) -> bool:

        clean = []

        for char in s:
            if char.isalnum():
                clean.append(char.lower())

        iteration = len(clean) // 2

        for i in range(0,iteration):
            if clean[i] != clean[-i - 1]:
                return False

        return True


# ---------------------------------------------------------------- tests


def palindrome(s: str) -> bool:
    return Solution().isPalindrome(s)


def test_example_1():
    assert palindrome("Was it a car or a cat I saw?") is True


def test_example_2():
    assert palindrome("tab a cat") is False


def test_single_character():
    assert palindrome("a") is True


def test_two_identical_characters():
    assert palindrome("aa") is True


def test_two_different_characters():
    assert palindrome("ab") is False


def test_nothing_alphanumeric_at_all():
    # everything is stripped, an empty string is a palindrome
    assert palindrome(".,!?") is True
    assert palindrome(" ") is True


def test_punctuation_between_the_letters():
    assert palindrome("A man, a plan, a canal: Panama") is True


def test_digits_count_as_alphanumeric():
    assert palindrome("12321") is True
    assert palindrome("12345") is False


def test_letters_and_digits_together():
    assert palindrome("1a2a1") is True


def test_digit_against_letter_is_not_equal():
    # the classic trap: '0' and 'P' are adjacent in ASCII case arithmetic
    assert palindrome("0P") is False


def test_case_is_ignored():
    assert palindrome("Aa") is True
    assert palindrome("RaceCar") is True


def test_odd_length_ignores_the_middle_character():
    assert palindrome("aba") is True
    assert palindrome("abXba") is True


def test_even_length_has_no_free_middle():
    assert palindrome("abba") is True
    assert palindrome("abca") is False


def test_difference_only_at_the_very_ends():
    assert palindrome("abcdefghijklmnopqrstuvwxyZ") is False


def test_long_palindrome_at_the_length_limit():
    half = "abcde" * 100          # 500 chars
    assert palindrome(half + half[::-1]) is True


if __name__ == "__main__":
    print(palindrome("Was it a car or a cat I saw?"))
