// 3652. Best Time to Buy and Sell Stock using Strategy · Medium · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/
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
    pub fn max_profit(prices: Vec<i32>, strategy: Vec<i32>, k: i32) -> i64 {
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
        assert_eq!(Solution::max_profit(vec![4, 2, 8], vec![-1, 0, 1], 2), 10);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::max_profit(vec![5, 4, 3], vec![1, 1, 0], 2), 9);
    }
}
