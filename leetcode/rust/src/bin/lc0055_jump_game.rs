// 55. Jump Game · Medium · https://leetcode.com/problems/jump-game/
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
    pub fn can_jump(nums: Vec<i32>) -> bool {
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
        assert_eq!(Solution::can_jump(vec![2, 3, 1, 1, 4]), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::can_jump(vec![3, 2, 1, 0, 4]), false);
    }
}
