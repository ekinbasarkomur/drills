// 470. Implement Rand10() Using Rand7() · Medium · https://leetcode.com/problems/implement-rand10-using-rand7/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// LeetCode provides rand7(); this one stands in for it.
inline int rand7() { static mt19937 g(42); return uniform_int_distribution<int>(1, 7)(g); }

// ---------------------------------------------------------------- solution
// The rand7() API is already defined for you.
// int rand7();
// @return a random integer in the range 1 to 7

class Solution {
public:
    int rand10() {
        TODO();
    }
};
// ---------------------------------------------------------------- tests

// No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
// Write your own below if you want a local check.
