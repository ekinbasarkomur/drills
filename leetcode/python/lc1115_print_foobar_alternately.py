"""
1115. Print FooBar Alternately · Medium · https://leetcode.com/problems/print-foobar-alternately/
Plan: Aşama 5 · Concurrency

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class FooBar:
    def __init__(self, n):
        raise NotImplementedError
        self.n = n


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printFoo() outputs "foo". Do not change or remove this line.
        	printFoo()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            
            # printBar() outputs "bar". Do not change or remove this line.
        	printBar()


# ---------------------------------------------------------------- tests

# No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
# Write your own below if you want a local check.
