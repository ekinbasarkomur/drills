"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/

Problem: repeatedly smash the two heaviest stones together. Equal weights
         destroy each other; otherwise the difference goes back in. Return
         what is left, or 0.
Note: You need the two largest values over and over, and the result goes
      straight back into the pool -- that is a max-heap, not a sort.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def last_stone_weight(stones: List[int]) -> int:
    return Solution().lastStoneWeight(stones)


def test_example_1():
    assert last_stone_weight([2, 3, 6, 2, 4]) == 1


def test_example_2():
    assert last_stone_weight([1, 2]) == 1


def test_no_stones():
    assert last_stone_weight([]) == 0


def test_one_stone_survives_untouched():
    assert last_stone_weight([7]) == 7


def test_two_equal_stones_annihilate():
    assert last_stone_weight([1, 1]) == 0


def test_two_equal_heavy_stones():
    assert last_stone_weight([3, 3]) == 0


def test_the_classic_leetcode_case():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1


def test_a_tie_then_a_leftover():
    # the two 10s cancel, leaving 4 and 2
    assert last_stone_weight([10, 4, 2, 10]) == 2


def test_odd_count_of_equal_stones():
    assert last_stone_weight([1, 1, 1]) == 1


def test_value_range_extremes():
    assert last_stone_weight([1000, 1000, 1000]) == 1000


def test_largest_allowed_input():
    # 1000 stones of equal weight: they pair off and cancel completely.
    stones = [1000] * 1000
    assert last_stone_weight(stones) == 0


if __name__ == "__main__":
    print(last_stone_weight([2, 3, 6, 2, 4]))
