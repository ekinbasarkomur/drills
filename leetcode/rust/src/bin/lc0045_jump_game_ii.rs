// 45. Jump Game II · Medium · https://leetcode.com/problems/jump-game-ii/
// Plan: Aşama 0 · Greedy
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn jump(nums: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::jump(vec![2, 3, 1, 1, 4]), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::jump(vec![2, 3, 0, 1, 4]), 2);
    }
}
