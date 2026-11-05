// 46. Permutations · Medium · https://leetcode.com/problems/permutations/
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
    pub fn permute(nums: Vec<i32>) -> Vec<Vec<i32>> {
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
        let want: Vec<Vec<i32>> = vec![vec![1, 2, 3], vec![1, 3, 2], vec![2, 1, 3], vec![2, 3, 1], vec![3, 1, 2], vec![3, 2, 1]];
        check_eq!(sort_outer(Solution::permute(vec![1, 2, 3])), sort_outer(want));
    }

    #[test]
    fn example_2() {
        let want: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 0]];
        check_eq!(sort_outer(Solution::permute(vec![0, 1])), sort_outer(want));
    }

    #[test]
    fn example_3() {
        let want: Vec<Vec<i32>> = vec![vec![1]];
        check_eq!(sort_outer(Solution::permute(vec![1])), sort_outer(want));
    }
}
