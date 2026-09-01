"""
242. Valid Anagram           https://leetcode.com/problems/valid-anagram/

Problem: return True if t is a rearrangement of s.
Approach:
Time O(?), space O(?)
"""


def is_anagram(s: str, t: str) -> bool:
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_example_1():
    assert is_anagram("racecar", "carrace") is True


def test_example_2():
    assert is_anagram("jar", "jam") is False


def test_example_3():
    assert is_anagram("x", "x") is True


def test_different_lengths():
    assert is_anagram("ab", "abc") is False


def test_same_letters_different_counts():
    assert is_anagram("aab", "abb") is False


def test_identical_strings():
    assert is_anagram("anagram", "anagram") is True


def test_no_letters_in_common():
    assert is_anagram("abc", "xyz") is False


if __name__ == "__main__":
    print(is_anagram("racecar", "carrace"))
