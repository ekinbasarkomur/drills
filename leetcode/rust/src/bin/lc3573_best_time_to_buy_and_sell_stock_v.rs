// 3573. Best Time to Buy and Sell Stock V · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn maximum_profit(prices: Vec<i32>, k: i32) -> i64 {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        assert_eq!(Solution::maximum_profit(vec![1, 7, 9, 8, 2], 2), 14);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::maximum_profit(vec![12, 16, 19, 19, 8, 1, 19, 13, 9], 3), 36);
    }
}
