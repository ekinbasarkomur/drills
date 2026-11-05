// 35. Search Insert Position · Easy · https://leetcode.com/problems/search-insert-position/
// Plan: Aşama 0 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn search_insert(nums: Vec<i32>, target: i32) -> i32 {
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
        check_eq!(Solution::search_insert(vec![1, 3, 5, 6], 5), 2);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::search_insert(vec![1, 3, 5, 6], 2), 1);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::search_insert(vec![1, 3, 5, 6], 7), 4);
    }
}
