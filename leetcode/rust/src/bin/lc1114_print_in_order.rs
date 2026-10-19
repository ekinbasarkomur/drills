// 1114. Print in Order · Easy · https://leetcode.com/problems/print-in-order/
// Plan: Aşama 5 · Concurrency
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Foo {
    
}

impl Foo {
    fn new() -> Self {
        Foo {
            
        }
    }

    fn first<F>(&self, print_first: F)
    where
        F: FnOnce(),
    {
        todo!();
        // Do not change this line
        print_first();
    }

    fn second<F>(&self, print_second: F)
    where
        F: FnOnce(),
    {
        // Do not change this line
        print_second();
    }

    fn third<F>(&self, print_third: F)
    where
        F: FnOnce(),
    {
        // Do not change this line
        print_third();
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

// No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
// Write your own below if you want a local check.
