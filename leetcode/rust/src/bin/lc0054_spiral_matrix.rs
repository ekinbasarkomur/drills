// 54. Spiral Matrix · Medium · https://leetcode.com/problems/spiral-matrix/
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
    pub fn spiral_order(matrix: Vec<Vec<i32>>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![1, 2, 3, 6, 9, 8, 7, 4, 5];
        check_eq!(Solution::spiral_order(vec![vec![1, 2, 3], vec![4, 5, 6], vec![7, 8, 9]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7];
        check_eq!(Solution::spiral_order(vec![vec![1, 2, 3, 4], vec![5, 6, 7, 8], vec![9, 10, 11, 12]]), want);
    }
}
