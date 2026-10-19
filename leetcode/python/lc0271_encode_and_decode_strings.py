"""
271. Encode and Decode Strings
https://leetcode.com/problems/encode-and-decode-strings/
Plan: Aşama 0 · Arrays & Hashing

Problem: turn a list of strings into ONE string, and turn it back. The strings
         may contain any ASCII character -- including whatever separator you
         were about to reach for.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def encode(self, strs: list[str]) -> str:
        raise NotImplementedError

    def decode(self, s: str) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

# The tests below call the old free functions; forward them to Solution.
def encode(*args): return Solution().encode(*args)  # noqa: E704
def decode(*args): return Solution().decode(*args)  # noqa: E704
# The encoding format is yours to choose, so the tests never look at the
# encoded string. They only check that decode(encode(x)) == x.


def _roundtrip(strs: list[str]) -> None:
    assert decode(encode(list(strs))) == strs


def test_example_1():
    _roundtrip(["Hello", "World"])


def test_example_2():
    _roundtrip([""])


def test_empty_list():
    _roundtrip([])


def test_several_empty_strings():
    _roundtrip(["", "", ""])


def test_empty_string_between_real_ones():
    _roundtrip(["a", "", "b"])


def test_single_string():
    _roundtrip(["lonely"])


# The interesting cases: the payload contains whatever you picked as a
# separator, or text that looks like your own length header.


def test_payload_contains_hash():
    _roundtrip(["a#b", "#", "##"])


def test_payload_looks_like_a_length_header():
    _roundtrip(["3#abc", "12#", "0#"])


def test_payload_contains_digits_and_punctuation():
    _roundtrip(["123", ",", ";", "|", ":", "\\"])


def test_payload_contains_whitespace_and_newlines():
    _roundtrip(["a b", "\n", "\t\t", " ", "line1\nline2"])


def test_long_strings_at_the_length_limit():
    _roundtrip(["x" * 199, "#" * 199])


def test_many_strings():
    _roundtrip([f"item{i}" for i in range(99)])


if __name__ == "__main__":
    wire = encode(["Hello", "World"])
    print(repr(wire))
    print(decode(wire))
