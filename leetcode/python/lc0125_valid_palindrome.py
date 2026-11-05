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
    check(palindrome("Was it a car or a cat I saw?"), True, 'palindrome("Was it a car or a cat I saw?")', op="is")


def test_example_2():
    check(palindrome("tab a cat"), False, 'palindrome("tab a cat")', op="is")


def test_single_character():
    check(palindrome("a"), True, 'palindrome("a")', op="is")


def test_two_identical_characters():
    check(palindrome("aa"), True, 'palindrome("aa")', op="is")


def test_two_different_characters():
    check(palindrome("ab"), False, 'palindrome("ab")', op="is")


def test_nothing_alphanumeric_at_all():
    # everything is stripped, an empty string is a palindrome
    check(palindrome(".,!?"), True, 'palindrome(".,!?")', op="is")
    check(palindrome(" "), True, 'palindrome(" ")', op="is")


def test_punctuation_between_the_letters():
    check(palindrome("A man, a plan, a canal: Panama"), True, 'palindrome("A man, a plan, a canal: Panama")', op="is")


def test_digits_count_as_alphanumeric():
    check(palindrome("12321"), True, 'palindrome("12321")', op="is")
    check(palindrome("12345"), False, 'palindrome("12345")', op="is")


def test_letters_and_digits_together():
    check(palindrome("1a2a1"), True, 'palindrome("1a2a1")', op="is")


def test_digit_against_letter_is_not_equal():
    # the classic trap: '0' and 'P' are adjacent in ASCII case arithmetic
    check(palindrome("0P"), False, 'palindrome("0P")', op="is")


def test_case_is_ignored():
    check(palindrome("Aa"), True, 'palindrome("Aa")', op="is")
    check(palindrome("RaceCar"), True, 'palindrome("RaceCar")', op="is")


def test_odd_length_ignores_the_middle_character():
    check(palindrome("aba"), True, 'palindrome("aba")', op="is")
    check(palindrome("abXba"), True, 'palindrome("abXba")', op="is")


def test_even_length_has_no_free_middle():
    check(palindrome("abba"), True, 'palindrome("abba")', op="is")
    check(palindrome("abca"), False, 'palindrome("abca")', op="is")


def test_difference_only_at_the_very_ends():
    check(palindrome("abcdefghijklmnopqrstuvwxyZ"), False, 'palindrome("abcdefghijklmnopqrstuvwxyZ")', op="is")


def test_long_palindrome_at_the_length_limit():
    half = "abcde" * 100          # 500 chars
    check(palindrome(half + half[::-1]), True, "palindrome(half + half[::-1])", op="is")


if __name__ == "__main__":
    print(palindrome("Was it a car or a cat I saw?"))
