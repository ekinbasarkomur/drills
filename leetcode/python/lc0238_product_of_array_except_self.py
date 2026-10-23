"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
Plan: Aşama 0 · Arrays & Hashing

Problem: output[i] is the product of every element of nums except nums[i].
Approach: build a prefix table (product of everything to the left of i) and a
          suffix table (product of everything to the right), then multiply them
          position by position. No division, so a zero in the input is harmless.
          Time O(n), space O(n).
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1]
        suffix = [1]

        number_len = len(nums)

        for index, number in enumerate(nums):
            prefix.append(prefix[index] * number)
            suffix.append(suffix[index] * nums[number_len - index - 1])

        prefix = prefix[:-1]
        suffix = suffix[:-1]
        suffix = list(reversed(suffix))

        for i in range(0, number_len):
            output.append(prefix[i] * suffix[i])

        return output
# ---------------------------------------------------------------- tests


def product_except_self(nums: list[int]) -> list[int]:
    return Solution().productExceptSelf(nums)


def test_example_1():
    assert product_except_self([1, 2, 4, 6]) == [48, 24, 12, 8]


def test_example_2():
    assert product_except_self([-1, 0, 1, 2, 3]) == [0, -6, 0, 0, 0]


def test_shortest_possible_input():
    assert product_except_self([2, 3]) == [3, 2]


def test_all_ones():
    assert product_except_self([1, 1, 1, 1]) == [1, 1, 1, 1]


# The two cases a naive "divide by nums[i]" solution gets wrong.


def test_one_zero_in_the_middle():
    assert product_except_self([1, 2, 0, 4]) == [0, 0, 8, 0]


def test_two_zeros_make_everything_zero():
    assert product_except_self([0, 4, 0, 5]) == [0, 0, 0, 0]


def test_zero_at_each_end():
    assert product_except_self([0, 3, 5]) == [15, 0, 0]
    assert product_except_self([3, 5, 0]) == [0, 0, 15]


def test_negative_numbers_flip_the_sign():
    assert product_except_self([-1, -2, -3]) == [6, 3, 2]
    assert product_except_self([-2, 3, -4]) == [-12, 8, -6]


def test_value_range_extremes():
    assert product_except_self([-30, 30]) == [30, -30]


def test_large_input_stays_linear():
    # 100_000 elements: anything O(n^2) will hang here rather than fail.
    n = 100_000
    nums = [1] * n
    nums[7] = 0

    out = product_except_self(nums)

    assert len(out) == n
    assert out[7] == 1
    assert all(v == (1 if i == 7 else 0) for i, v in enumerate(out))


if __name__ == "__main__":
    print(product_except_self([1, 2, 4, 6]))
