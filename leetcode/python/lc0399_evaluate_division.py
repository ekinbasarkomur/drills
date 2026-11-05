"""
399. Evaluate Division · Medium · https://leetcode.com/problems/evaluate-division/
Plan: Aşama 5 · Olasılık ve Matematik

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    check_true(close(Solution().calcEquation([['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]), [6.0, 0.5, -1.0, 1.0, -1.0]), "close(Solution().calcEquation([['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a'], ['x', 'x']]), [6.0, 0.5, -1.0, 1.0, -1.0])")


def test_example_2():
    check_true(close(Solution().calcEquation([['a', 'b'], ['b', 'c'], ['bc', 'cd']], [1.5, 2.5, 5.0], [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]), [3.75, 0.4, 5.0, 0.2]), "close(Solution().calcEquation([['a', 'b'], ['b', 'c'], ['bc', 'cd']], [1.5, 2.5, 5.0], [['a', 'c'], ['c', 'b'], ['bc', 'cd'], ['cd', 'bc']]), [3.75, 0.4, 5.0, 0.2])")


def test_example_3():
    check_true(close(Solution().calcEquation([['a', 'b']], [0.5], [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]), [0.5, 2.0, -1.0, -1.0]), "close(Solution().calcEquation([['a', 'b']], [0.5], [['a', 'b'], ['b', 'a'], ['a', 'c'], ['x', 'y']]), [0.5, 2.0, -1.0, -1.0])")
