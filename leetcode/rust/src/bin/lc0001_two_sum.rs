// 1. Two Sum                   https://leetcode.com/problems/two-sum/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return the two indices whose values add up to target, smaller first.
// Approach: one pass. For each number, record the *complement* it needs
//           (target - num) as a key pointing at the current index. When a later
//           number turns out to be a complement someone asked for, that earlier
//           index and the current one are the answer.
//           Time O(n), space O(n).

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen : HashMap<i32, usize> = HashMap::new();

        for i in 0..nums.len()
        {
            let diff = target - nums[i];

            if seen.contains_key(&diff)
            {
                return vec!(i as i32, seen[&diff as &i32] as i32);
            }

            seen.insert(nums[i], i);

        }

        return vec!();
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::two_sum(vec![3, 4, 5, 6], 7));
    println!("{:?}", Solution::two_sum(vec![4, 5, 6], 10));
    println!("{:?}", Solution::two_sum(vec![5, 5], 10));
}

#[cfg(test)]
mod tests {
    use super::*;

    // LeetCode accepts the two indices in either order, so compare them sorted.
    fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut got = Solution::two_sum(nums, target);
        got.sort();
        got
    }

    #[test]
    fn example_1() {
        check_eq!(two_sum(vec![3, 4, 5, 6], 7), vec![0, 1]);
    }

    #[test]
    fn example_2() {
        check_eq!(two_sum(vec![4, 5, 6], 10), vec![0, 2]);
    }

    #[test]
    fn example_3() {
        check_eq!(two_sum(vec![5, 5], 10), vec![0, 1]);
    }

    #[test]
    fn answer_is_the_last_two() {
        check_eq!(two_sum(vec![1, 9, 3, 4], 7), vec![2, 3]);
    }

    #[test]
    fn negative_numbers() {
        check_eq!(two_sum(vec![-3, 4, 7, -1], -4), vec![0, 3]);
    }

    #[test]
    fn target_is_zero() {
        check_eq!(two_sum(vec![-8, 2, 8], 0), vec![0, 2]);
    }

    #[test]
    fn extreme_values() {
        check_eq!(
            two_sum(vec![10_000_000, -10_000_000, 3], 0),
            vec![0, 1]
        );
    }
}
