// 3161. Block Placement Queries · Hard · https://leetcode.com/problems/block-placement-queries/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn get_results(queries: Vec<Vec<i32>>) -> Vec<bool> {
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
        let want: Vec<bool> = vec![false, true, true];
        assert_eq!(Solution::get_results(vec![vec![1, 2], vec![2, 3, 3], vec![2, 3, 1], vec![2, 2, 2]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<bool> = vec![true, true, false];
        assert_eq!(Solution::get_results(vec![vec![1, 7], vec![2, 7, 6], vec![1, 2], vec![2, 7, 5], vec![2, 7, 6]]), want);
    }
}
