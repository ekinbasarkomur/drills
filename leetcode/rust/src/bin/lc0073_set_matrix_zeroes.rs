// 73. Set Matrix Zeroes · Medium · https://leetcode.com/problems/set-matrix-zeroes/
// Plan: Aşama 0 · Matrix
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn set_zeroes(matrix: &mut Vec<Vec<i32>>) {
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
        let mut matrix: Vec<Vec<i32>> = vec![vec![1, 1, 1], vec![1, 0, 1], vec![1, 1, 1]];
        Solution::set_zeroes(&mut matrix);
        let want: Vec<Vec<i32>> = vec![vec![1, 0, 1], vec![0, 0, 0], vec![1, 0, 1]];
        check_eq!(matrix, want);
    }

    #[test]
    fn example_2() {
        let mut matrix: Vec<Vec<i32>> = vec![vec![0, 1, 2, 0], vec![3, 4, 5, 2], vec![1, 3, 1, 5]];
        Solution::set_zeroes(&mut matrix);
        let want: Vec<Vec<i32>> = vec![vec![0, 0, 0, 0], vec![0, 4, 5, 0], vec![0, 3, 1, 0]];
        check_eq!(matrix, want);
    }
}
