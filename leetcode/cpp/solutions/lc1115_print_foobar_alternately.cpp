// 1115. Print FooBar Alternately · Medium · https://leetcode.com/problems/print-foobar-alternately/
// Plan: Aşama 5 · Concurrency
//
// Problem:
// Approach:
// Time O(?), space O(?)

#include "leetcode.hpp"
#include "test.hpp"

// ---------------------------------------------------------------- solution
class FooBar {
private:
    int n;

public:
    FooBar(int n) {
        this->n = n;
    }

    void foo(function<void()> printFoo) {
        TODO();
        for (int i = 0; i < n; i++) {
            
        	// printFoo() outputs "foo". Do not change or remove this line.
        	printFoo();
        }
    }

    void bar(function<void()> printBar) {
        TODO();
        for (int i = 0; i < n; i++) {
            
        	// printBar() outputs "bar". Do not change or remove this line.
        	printBar();
        }
    }
};
// ---------------------------------------------------------------- tests

// No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
// Write your own below if you want a local check.
