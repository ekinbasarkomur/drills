// 322. Coin Change · Medium · https://leetcode.com/problems/coin-change/
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
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
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
        check_eq!(Solution::coin_change(vec![1, 2, 5], 11), 3);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::coin_change(vec![2], 3), -1);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::coin_change(vec![1], 0), 0);
    }
}
