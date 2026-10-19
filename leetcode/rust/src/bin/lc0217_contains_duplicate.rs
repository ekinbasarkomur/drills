// 217. Contains Duplicate      https://leetcode.com/problems/contains-duplicate/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return true if any value appears more than once in nums.
// Approach: walk the array once, keep every number seen so far in a HashSet.
//           If the current number is already in the set, we found a duplicate.
//           Time O(n), space O(n).

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::collections::HashSet;

impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let len = nums.len();
        let mut numbers: HashSet<i32> = HashSet::with_capacity(nums.len());

        for i in 0..len {
            if numbers.contains(&nums[i]) {
                return true;
            }
            numbers.insert(nums[i]);
        }
        return false;
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::has_duplicate(vec![1, 2, 3, 3]));
    println!("{}", Solution::has_duplicate(vec![1, 2, 3, 4]));
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        assert!(Solution::has_duplicate(vec![1, 2, 3, 3]));
    }

    #[test]
    fn example_2() {
        assert!(!Solution::has_duplicate(vec![1, 2, 3, 4]));
    }

    #[test]
    fn empty_array() {
        assert!(!Solution::has_duplicate(vec![]));
    }

    #[test]
    fn single_element() {
        assert!(!Solution::has_duplicate(vec![7]));
    }

    #[test]
    fn duplicate_at_the_very_end() {
        assert!(Solution::has_duplicate(vec![1, 2, 3, 4, 5, 1]));
    }

    #[test]
    fn negatives_and_extremes() {
        assert!(Solution::has_duplicate(vec![
            -1_000_000_000,
            0,
            -1_000_000_000
        ]));
        assert!(!Solution::has_duplicate(vec![
            -1_000_000_000,
            1_000_000_000
        ]));
    }
}
