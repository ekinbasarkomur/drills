// 877. Stone Game · Medium · https://leetcode.com/problems/stone-game/
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
    pub fn stone_game(piles: Vec<i32>) -> bool {
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
        assert_eq!(Solution::stone_game(vec![5, 3, 4, 5]), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::stone_game(vec![3, 7, 2, 3]), true);
    }
}
