"""
1268. Search Suggestions System · Medium · https://leetcode.com/problems/search-suggestions-system/
Plan: Aşama 3 · Order Book ve Sistem Tasarımı

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def suggestedProducts(self, products: list[str], searchWord: str) -> list[list[str]]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check(Solution().suggestedProducts(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse'), [['mobile', 'moneypot', 'monitor'], ['mobile', 'moneypot', 'monitor'], ['mouse', 'mousepad'], ['mouse', 'mousepad'], ['mouse', 'mousepad']], "Solution().suggestedProducts(['mobile', 'mouse', 'moneypot', 'monitor', 'mousepad'], 'mouse')")


def test_example_2():
    check(Solution().suggestedProducts(['havana'], 'havana'), [['havana'], ['havana'], ['havana'], ['havana'], ['havana'], ['havana']], "Solution().suggestedProducts(['havana'], 'havana')")
