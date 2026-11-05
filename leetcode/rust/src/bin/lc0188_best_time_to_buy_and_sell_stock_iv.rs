// 188. Best Time to Buy and Sell Stock IV · Hard · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
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
    pub fn max_profit(k: i32, prices: Vec<i32>) -> i32 {
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
        check_eq!(Solution::max_profit(2, vec![2, 4, 1]), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::max_profit(2, vec![3, 2, 6, 5, 0, 3]), 7);
    }
}
