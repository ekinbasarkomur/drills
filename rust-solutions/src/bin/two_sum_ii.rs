// 167. Two Sum II - Input Array Is Sorted
// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
//
// Problem: numbers is sorted ascending. Return the ONE-BASED indices of the two
//          values that add up to target, smaller index first. Exactly one
//          answer exists and you may not use the same element twice.
// Follow-up: constant extra space -- so no HashMap this time.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let _ = (numbers, target);
        todo!()
    }
}

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
        assert_eq!(two_sum(&[1, 2, 3, 4], 3), vec![1, 2]);
    }

    #[test]
    fn example_2() {
        assert_eq!(two_sum(&[2, 7, 11, 15], 9), vec![1, 2]);
    }

    #[test]
    fn example_3() {
        assert_eq!(two_sum(&[2, 3, 4], 6), vec![1, 3]);
    }

    #[test]
    fn shortest_possible_input() {
        assert_eq!(two_sum(&[-1, 0], -1), vec![1, 2]);
    }

    #[test]
    fn the_two_ends_are_the_answer() {
        assert_eq!(two_sum(&[1, 2, 3, 4, 5, 6, 7], 8), vec![1, 7]);
    }

    #[test]
    fn the_answer_sits_in_the_middle() {
        assert_eq!(two_sum(&[1, 2, 3, 4, 5, 6, 7], 7), vec![3, 4]);
    }

    #[test]
    fn equal_values_next_to_each_other() {
        assert_eq!(two_sum(&[3, 3], 6), vec![1, 2]);
    }

    #[test]
    fn repeated_values_around_the_answer() {
        assert_eq!(two_sum(&[1, 1, 1, 5, 9], 6), vec![3, 4]);
    }

    #[test]
    fn all_negative() {
        assert_eq!(two_sum(&[-9, -7, -3, -1], -10), vec![2, 3]);
    }

    #[test]
    fn crossing_zero() {
        assert_eq!(two_sum(&[-5, -2, 0, 3, 8], 3), vec![2, 5]);
    }

    #[test]
    fn target_is_zero() {
        assert_eq!(two_sum(&[-4, -1, 0, 1, 4], 0), vec![2, 4]);
    }

    #[test]
    fn value_range_extremes() {
        assert_eq!(two_sum(&[-1000, 0, 1000], 0), vec![1, 3]);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 elements: the answer is the very first and the very last, so a
        // scan that starts from both ends finds it immediately while a nested
        // loop grinds through the whole array.
        let n = 1000;
        let numbers: Vec<i32> = (0..n).collect();
        assert_eq!(two_sum(&numbers, n - 1), vec![1, n as i32]);
    }
}
