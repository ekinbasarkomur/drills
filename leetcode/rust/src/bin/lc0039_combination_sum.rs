// 39. Combination Sum · Medium · https://leetcode.com/problems/combination-sum/
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
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
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
        let want: Vec<Vec<i32>> = vec![vec![2, 2, 3], vec![7]];
        check_eq!(deep_sort(Solution::combination_sum(vec![2, 3, 6, 7], 7)), deep_sort(want));
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<i32>> = vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]];
        check_eq!(deep_sort(Solution::combination_sum(vec![2, 3, 5], 8)), deep_sort(want));
    }

    #[test]
    fn example_3() {
        let want: Vec<Vec<i32>> = vec![];
        check_eq!(deep_sort(Solution::combination_sum(vec![2], 1)), deep_sort(want));
    }
}
