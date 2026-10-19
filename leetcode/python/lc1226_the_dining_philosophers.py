"""
1226. The Dining Philosophers · Medium · https://leetcode.com/problems/the-dining-philosophers/
Plan: Aşama 5 · Concurrency

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class DiningPhilosophers:

    # call the functions directly to execute, for example, eat()
    def wantsToEat(self,
                   philosopher: int,
                   pickLeftFork: 'Callable[[], None]',
                   pickRightFork: 'Callable[[], None]',
                   eat: 'Callable[[], None]',
                   putLeftFork: 'Callable[[], None]',
                   putRightFork: 'Callable[[], None]') -> None:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

# No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
# Write your own below if you want a local check.
