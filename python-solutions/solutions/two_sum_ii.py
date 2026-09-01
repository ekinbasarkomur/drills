"""
167. Two Sum II - Input Array Is Sorted
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
         values that add up to target, smaller index first. Exactly one answer
         exists and you may not use the same element twice.
Follow-up: constant extra space -- so no dict this time.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def two_sum(numbers: list[int], target: int) -> list[int]:
    return Solution().twoSum(numbers, target)


def test_example_1():
    assert two_sum([1, 2, 3, 4], 3) == [1, 2]


def test_example_2():
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]


def test_example_3():
    assert two_sum([2, 3, 4], 6) == [1, 3]


def test_shortest_possible_input():
    assert two_sum([-1, 0], -1) == [1, 2]


def test_the_two_ends_are_the_answer():
    assert two_sum([1, 2, 3, 4, 5, 6, 7], 8) == [1, 7]


def test_the_answer_sits_in_the_middle():
    assert two_sum([1, 2, 3, 4, 5, 6, 7], 7) == [3, 4]


def test_equal_values_next_to_each_other():
    assert two_sum([3, 3], 6) == [1, 2]


def test_repeated_values_around_the_answer():
    assert two_sum([1, 1, 1, 5, 9], 6) == [3, 4]


def test_all_negative():
    assert two_sum([-9, -7, -3, -1], -10) == [2, 3]


def test_crossing_zero():
    assert two_sum([-5, -2, 0, 3, 8], 3) == [2, 5]


def test_target_is_zero():
    assert two_sum([-4, -1, 0, 1, 4], 0) == [2, 4]


def test_value_range_extremes():
    assert two_sum([-1000, 0, 1000], 0) == [1, 3]


def test_largest_allowed_input():
    # 1000 elements: the answer is the very first and the very last, so a scan
    # that starts from both ends finds it immediately while a nested loop
    # grinds through the whole array.
    n = 1000
    numbers = list(range(n))
    assert two_sum(numbers, n - 1) == [1, n]


if __name__ == "__main__":
    print(two_sum([1, 2, 3, 4], 3))
