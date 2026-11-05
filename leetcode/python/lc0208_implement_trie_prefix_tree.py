"""
208. Implement Trie (Prefix Tree) · Medium · https://leetcode.com/problems/implement-trie-prefix-tree/
Plan: Aşama 4 · Graph

Problem:
Approach:
Time O(?), space O(?)
"""

from _lc import *  # noqa: F403  (LeetCode's namespace: List, ListNode, ...)

# ---------------------------------------------------------------- solution
class Trie:

    def __init__(self):
        raise NotImplementedError
    def insert(self, word: str) -> None:
        raise NotImplementedError
    def search(self, word: str) -> bool:
        raise NotImplementedError
    def startsWith(self, prefix: str) -> bool:
        raise NotImplementedError
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


# ---------------------------------------------------------------- tests

def test_example_1():
    obj = Trie()
    obj.insert('apple')
    check(obj.search('apple'), True, "obj.search('apple')")
    check(obj.search('app'), False, "obj.search('app')")
    check(obj.startsWith('app'), True, "obj.startsWith('app')")
    obj.insert('app')
    check(obj.search('app'), True, "obj.search('app')")
