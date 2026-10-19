// 1115. Print FooBar Alternately · Medium · https://leetcode.com/problems/print-foobar-alternately/
// Plan: Aşama 5 · Concurrency
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct FooBar {
    n: usize,
}

impl FooBar {
    fn new(n: usize) -> Self {
        FooBar { n }
    }

    fn foo<F>(&self, print_foo: F)
    where
        F: Fn(),
    {
        todo!();
        for _ in 0..self.n {
            // printFoo() outputs "foo". Do not change or remove this line.
            print_foo();
        }
    }

    fn bar<F>(&self, print_bar: F)
    where
        F: Fn(),
    {
        for _ in 0..self.n {
            // printBar() outputs "bar". Do not change or remove this line.
            print_bar();
        }
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

// No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
// Write your own below if you want a local check.
