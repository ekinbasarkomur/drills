// 78. Subsets · Medium · https://leetcode.com/problems/subsets/
// Plan: Aşama 4 · Backtracking
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn subsets(nums: Vec<i32>) -> Vec<Vec<i32>> {
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
        let want: Vec<Vec<i32>> = vec![vec![], vec![1], vec![2], vec![1, 2], vec![3], vec![1, 3], vec![2, 3], vec![1, 2, 3]];
        assert_eq!(deep_sort(Solution::subsets(vec![1, 2, 3])), deep_sort(want));
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<i32>> = vec![vec![], vec![0]];
        assert_eq!(deep_sort(Solution::subsets(vec![0])), deep_sort(want));
    }
}
