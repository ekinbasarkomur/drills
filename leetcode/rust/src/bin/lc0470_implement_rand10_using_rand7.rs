// 470. Implement Rand10() Using Rand7() · Medium · https://leetcode.com/problems/implement-rand10-using-rand7/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// LeetCode provides rand7(); this one stands in for it.
fn rand7() -> i32 {
    rand::random_range(1..=7)
}

// ---------------------------------------------------------------- solution
/** 
 * The rand7() API is already defined for you.
 * @return a random integer in the range 1 to 7
 * fn rand7() -> i32;
 */

impl Solution {
    pub fn rand10() -> i32 {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

// No tests were generated: LeetCode judges this one with a custom checker (concurrency, randomness or a hidden harness).
// Write your own below if you want a local check.
