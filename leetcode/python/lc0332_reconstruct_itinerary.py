"""
332. Reconstruct Itinerary · Hard · https://leetcode.com/problems/reconstruct-itinerary/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    assert Solution().findItinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]) == ['JFK', 'MUC', 'LHR', 'SFO', 'SJC']


def test_example_2():
    assert Solution().findItinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]) == ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
