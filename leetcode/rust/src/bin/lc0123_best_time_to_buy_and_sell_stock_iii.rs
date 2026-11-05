// 123. Best Time to Buy and Sell Stock III · Hard · https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
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
    pub fn max_profit(prices: Vec<i32>) -> i32 {
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
        check_eq!(Solution::max_profit(vec![3, 3, 5, 0, 0, 3, 1, 4]), 6);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::max_profit(vec![1, 2, 3, 4, 5]), 4);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::max_profit(vec![7, 6, 4, 3, 1]), 0);
    }
}
