// 765. Couples Holding Hands · Hard · https://leetcode.com/problems/couples-holding-hands/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn min_swaps_couples(row: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::min_swaps_couples(vec![0, 2, 1, 3]), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::min_swaps_couples(vec![3, 2, 0, 1]), 0);
    }
}
