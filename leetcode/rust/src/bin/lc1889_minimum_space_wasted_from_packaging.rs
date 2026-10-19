// 1889. Minimum Space Wasted From Packaging · Hard · https://leetcode.com/problems/minimum-space-wasted-from-packaging/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn min_wasted_space(packages: Vec<i32>, boxes: Vec<Vec<i32>>) -> i32 {
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
        assert_eq!(Solution::min_wasted_space(vec![2, 3, 5], vec![vec![4, 8], vec![2, 8]]), 6);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::min_wasted_space(vec![2, 3, 5], vec![vec![1, 4], vec![2, 3], vec![3, 4]]), -1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::min_wasted_space(vec![3, 5, 8, 10, 11, 12], vec![vec![12], vec![11, 9], vec![10, 5, 14]]), 9);
    }
}
