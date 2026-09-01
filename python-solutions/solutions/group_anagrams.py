"""
49. Group Anagrams           https://leetcode.com/problems/group-anagrams/

Problem: bucket the input strings so that anagrams end up in the same sublist.
Approach:
Time O(?), space O(?)
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    raise NotImplementedError


# ---------------------------------------------------------------- tests
# The output may come back in any order, so sort both levels before comparing.


def _normalized(strs: list[str]) -> list[list[str]]:
    return sorted(sorted(group) for group in group_anagrams(strs))


def _expected(groups: list[list[str]]) -> list[list[str]]:
    return sorted(sorted(group) for group in groups)


def test_example_1():
    got = _normalized(["act", "pots", "tops", "cat", "stop", "hat"])
    assert got == _expected([["hat"], ["act", "cat"], ["stop", "pots", "tops"]])


def test_example_2():
    assert _normalized(["x"]) == _expected([["x"]])


def test_example_3():
    assert _normalized([""]) == _expected([[""]])


def test_no_two_words_are_anagrams():
    assert _normalized(["abc", "de", "f"]) == _expected([["abc"], ["de"], ["f"]])


def test_everything_in_one_group():
    assert _normalized(["abc", "bca", "cab"]) == _expected([["abc", "bca", "cab"]])


def test_duplicates_stay_as_separate_entries():
    assert _normalized(["ab", "ab", "ba"]) == _expected([["ab", "ab", "ba"]])


def test_repeated_letters_are_not_confused():
    # same letter set, different counts -> different groups
    assert _normalized(["aab", "abb"]) == _expected([["aab"], ["abb"]])


def test_several_empty_strings_group_together():
    assert _normalized(["", "", "a"]) == _expected([["", ""], ["a"]])


if __name__ == "__main__":
    print(group_anagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
