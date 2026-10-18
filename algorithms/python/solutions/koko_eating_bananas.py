"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Problem: find the smallest eating rate k such that every pile is
         finished within h hours. A pile takes ceil(pile / k) hours, and
         leftover time in an hour is wasted -- no starting the next pile.
Note: You are not searching the array, you are searching the ANSWER: every
      rate from 1 to max(piles) either works or does not, and once one
      works every larger one does too.
Approach:
Time O(?), space O(?)
"""

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        raise NotImplementedError


# ---------------------------------------------------------------- tests


def min_eating_speed(piles: List[int], h: int) -> int:
    return Solution().minEatingSpeed(piles, h)


def test_example_1():
    assert min_eating_speed([1, 4, 3, 2], 9) == 2


def test_example_2():
    # h equals the pile count, so each pile must go in one hour
    assert min_eating_speed([25, 10, 23, 4], 4) == 25


def test_single_pile_single_hour():
    assert min_eating_speed([1], 1) == 1


def test_time_to_spare():
    # k never drops below 1
    assert min_eating_speed([1], 10) == 1


def test_the_classic_leetcode_case():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4


def test_tight_deadline():
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30


def test_one_hour_more_is_enough_to_slow_down():
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23


def test_uniform_piles():
    assert min_eating_speed([1, 1, 1, 1], 4) == 1


def test_value_range_extremes():
    # one pile of a billion in one hour -- the rate must match it exactly
    assert min_eating_speed([1000000000], 1) == 1000000000


def test_largest_allowed_input():
    # 10_000 piles of 10_000 bananas each and exactly 10_000 hours: one pile
    # per hour, so the rate has to be the pile size. Scanning k from 1
    # upwards would take 10_000 passes; binary search takes 14.
    piles = [10_000] * 10_000
    assert min_eating_speed(piles, 10_000) == 10000


if __name__ == "__main__":
    print(min_eating_speed([1, 4, 3, 2], 9))
