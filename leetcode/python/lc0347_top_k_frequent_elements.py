"""
347. Top K Frequent Elements
https://leetcode.com/problems/top-k-frequent-elements/
Plan: Aşama 0 · Arrays & Hashing

Problem: return the k most frequent values in nums. The answer is unique and
         may be returned in any order.
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        number_inventory = {}

        output = []

        nums.sort()

        for index, number in enumerate(nums):
            if number in number_inventory.keys():
                number_inventory[number] += 1
                continue

            number_inventory[number] = 1

        inventory = sorted(number_inventory.items(), key=lambda c: c[1], reverse=True)
        # print(inventory)

        for i in range(0, k):
            output.append(inventory[i][0])

        return output


# ---------------------------------------------------------------- tests

# The tests below call the old free functions; forward them to Solution.
def top_k_frequent(*args): return Solution().topKFrequent(*args)  # noqa: E704
# "You may return the output in any order" -> sort before comparing.


def _top_k(nums: list[int], k: int) -> list[int]:
    return sorted(top_k_frequent(nums, k))


def test_example_1():
    check(_top_k([1, 2, 2, 3, 3, 3], 2), [2, 3], "_top_k([1, 2, 2, 3, 3, 3], 2)")


def test_example_2():
    check(_top_k([7, 7], 1), [7], "_top_k([7, 7], 1)")


def test_single_element():
    check(_top_k([1], 1), [1], "_top_k([1], 1)")


def test_k_equals_number_of_distinct_values():
    check(_top_k([1, 1, 2, 2, 3], 3), [1, 2, 3], "_top_k([1, 1, 2, 2, 3], 3)")


def test_negative_values():
    check(_top_k([-1, -1, -1, -2, -2, 5], 2), [-2, -1], "_top_k([-1, -1, -1, -2, -2, 5], 2)")


def test_extremes_of_the_value_range():
    check(_top_k([1000, 1000, -1000, -1000, -1000, 7], 1), [-1000], "_top_k([1000, 1000, -1000, -1000, -1000, 7], 1)")


def test_least_frequent_values_are_excluded():
    check(_top_k([4, 4, 4, 4, 9, 9, 9, 1, 1, 6], 2), [4, 9], "_top_k([4, 4, 4, 4, 9, 9, 9, 1, 1, 6], 2)")


def test_every_value_appears_once_except_one():
    check(_top_k([5, 6, 7, 8, 8], 1), [8], "_top_k([5, 6, 7, 8, 8], 1)")


if __name__ == "__main__":
    print(top_k_frequent([1, 2, 2, 3, 3, 3], 2))
