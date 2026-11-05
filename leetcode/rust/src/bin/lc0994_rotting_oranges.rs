// 994. Rotting Oranges · Medium · https://leetcode.com/problems/rotting-oranges/
// Plan: Aşama 0 · Graphs
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn oranges_rotting(grid: Vec<Vec<i32>>) -> i32 {
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
        check_eq!(Solution::oranges_rotting(vec![vec![2, 1, 1], vec![1, 1, 0], vec![0, 1, 1]]), 4);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::oranges_rotting(vec![vec![2, 1, 1], vec![0, 1, 1], vec![1, 0, 1]]), -1);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::oranges_rotting(vec![vec![0, 2]]), 0);
    }
}
