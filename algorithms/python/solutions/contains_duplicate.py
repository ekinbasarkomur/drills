"""
217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/

Problem: return True if any value appears more than once in nums.
Approach: walk the array once, keep every number seen so far in a set.
          Time O(n), space O(n).
"""


def has_duplicate(nums: list[int]) -> bool:
    seen: set[int] = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ---------------------------------------------------------------- tests


def test_example_1():
    assert has_duplicate([1, 2, 3, 3]) is True


def test_example_2():
    assert has_duplicate([1, 2, 3, 4]) is False


def test_empty_array():
    assert has_duplicate([]) is False


def test_single_element():
    assert has_duplicate([7]) is False


def test_duplicate_at_the_very_end():
    assert has_duplicate([1, 2, 3, 4, 5, 1]) is True


def test_negatives_and_extremes():
    assert has_duplicate([-10**9, 0, -10**9]) is True
    assert has_duplicate([-10**9, 10**9]) is False


if __name__ == "__main__":
    print(has_duplicate([1, 2, 3, 3]))
