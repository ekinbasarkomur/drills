// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
// Plan: Aşama 0 · Two Pointers
//
// Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
//          values that add up to target, smaller index first. Exactly one
//          answer exists and you may not use the same element twice.
// Follow-up: constant extra space -- so no HashMap this time.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::cmp::Ordering;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut left: i32 = 0;
        let mut right: i32 = numbers.len() as i32 - 1;

        while left < right {
            match target.cmp(&(numbers[left as usize] + numbers[right as usize] as i32)) {
                Ordering::Greater => left += 1,
                Ordering::Equal => return vec![left as i32 + 1, right as i32 + 1],
                Ordering::Less => right -= 1,
            }
        }
        vec![]
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::two_sum(vec![1, 2, 3, 4], 3));
    println!("{:?}", Solution::two_sum(vec![2, 7, 11, 15], 9));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn two_sum(numbers: &[i32], target: i32) -> Vec<i32> {
        Solution::two_sum(numbers.to_vec(), target)
    }

    #[test]
    fn example_1() {
        check_eq!(two_sum(&[1, 2, 3, 4], 3), vec![1, 2]);
    }

    #[test]
    fn example_2() {
        check_eq!(two_sum(&[2, 7, 11, 15], 9), vec![1, 2]);
    }

    #[test]
    fn example_3() {
        check_eq!(two_sum(&[2, 3, 4], 6), vec![1, 3]);
    }

    #[test]
    fn shortest_possible_input() {
        check_eq!(two_sum(&[-1, 0], -1), vec![1, 2]);
    }

    #[test]
    fn the_two_ends_are_the_answer() {
        check_eq!(two_sum(&[1, 5, 6, 7, 20], 21), vec![1, 5]);
    }

    #[test]
    fn the_answer_sits_in_the_middle() {
        check_eq!(two_sum(&[1, 4, 5, 6, 20], 11), vec![3, 4]);
    }

    #[test]
    fn equal_values_next_to_each_other() {
        check_eq!(two_sum(&[3, 3], 6), vec![1, 2]);
    }

    #[test]
    fn repeated_values_around_the_answer() {
        check_eq!(two_sum(&[2, 2, 3, 7], 10), vec![3, 4]);
    }

    #[test]
    fn all_negative() {
        check_eq!(two_sum(&[-9, -7, -3, -1], -4), vec![3, 4]);
    }

    #[test]
    fn crossing_zero() {
        check_eq!(two_sum(&[-5, -2, 0, 3, 8], 6), vec![2, 5]);
    }

    #[test]
    fn target_is_zero() {
        check_eq!(two_sum(&[-4, -1, 0, 1, 5], 0), vec![2, 4]);
    }

    #[test]
    fn value_range_extremes() {
        check_eq!(two_sum(&[-1000, 0, 1000], 0), vec![1, 3]);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 elements: the answer is the very first and the very last, so a
        // scan that starts from both ends finds it immediately while a nested
        // loop grinds through the whole array.
        let numbers: Vec<i32> = (0..1000).collect();
        // 998 + 999 is the only pair reaching 1997, and it sits at the far end
        check_eq!(two_sum(&numbers, 1997), vec![999, 1000]);
    }
}
