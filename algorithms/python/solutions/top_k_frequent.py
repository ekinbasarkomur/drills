"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/

Problem: return the k most frequent values in nums. The answer is unique and
         may be returned in any order.
Approach:
Time O(?), space O(?)
"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    raise NotImplementedError


# ---------------------------------------------------------------- tests
# "You may return the output in any order" -> sort before comparing.


def _top_k(nums: list[int], k: int) -> list[int]:
    return sorted(top_k_frequent(nums, k))


def test_example_1():
    assert _top_k([1, 2, 2, 3, 3, 3], 2) == [2, 3]


def test_example_2():
    assert _top_k([7, 7], 1) == [7]


def test_single_element():
    assert _top_k([1], 1) == [1]


def test_k_equals_number_of_distinct_values():
    assert _top_k([1, 1, 2, 2, 3], 3) == [1, 2, 3]


def test_negative_values():
    assert _top_k([-1, -1, -1, -2, -2, 5], 2) == [-2, -1]


def test_extremes_of_the_value_range():
    assert _top_k([1000, 1000, -1000, -1000, -1000, 7], 1) == [-1000]


def test_least_frequent_values_are_excluded():
    assert _top_k([4, 4, 4, 4, 9, 9, 9, 1, 1, 6], 2) == [4, 9]


def test_every_value_appears_once_except_one():
    assert _top_k([5, 6, 7, 8, 8], 1) == [8]


if __name__ == "__main__":
    print(top_k_frequent([1, 2, 2, 3, 3, 3], 2))
