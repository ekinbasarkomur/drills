// 33. Search in Rotated Sorted Array
// https://leetcode.com/problems/search-in-rotated-sorted-array/
//
// Problem: nums was sorted ascending, then rotated some number of times.
//          Return the index of target, or -1. O(log n) is the point.
// Note: At any midpoint one of the two halves is still properly sorted.
//       Work out which, and you know whether target can be in it.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        let _ = (nums, target,);
        todo!()
    }
}

fn main() {
    println!("{}", Solution::search(vec![3, 4, 5, 6, 1, 2], 1));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn search(nums: &[i32], target: i32) -> i32 {
        Solution::search(nums.to_vec(), target)
    }

    #[test]
    fn example_1() {
        assert_eq!(search(&[3, 4, 5, 6, 1, 2], 1), 4);
    }

    #[test]
    fn example_2() {
        assert_eq!(search(&[3, 5, 6, 0, 1, 2], 4), -1);
    }

    #[test]
    fn single_element_found() {
        assert_eq!(search(&[1], 1), 0);
    }

    #[test]
    fn single_element_missing() {
        assert_eq!(search(&[1], 2), -1);
    }

    #[test]
    fn not_rotated_at_all() {
        // a full rotation looks like no rotation
        assert_eq!(search(&[1, 2, 3, 4, 5, 6], 4), 3);
    }

    #[test]
    fn target_is_the_pivot() {
        assert_eq!(search(&[4, 5, 6, 7, 0, 1, 2], 0), 4);
    }

    #[test]
    fn target_missing_inside_the_range() {
        assert_eq!(search(&[4, 5, 6, 7, 0, 1, 2], 3), -1);
    }

    #[test]
    fn rotated_by_one() {
        assert_eq!(search(&[2, 1], 1), 1);
    }

    #[test]
    fn target_is_the_first_element() {
        assert_eq!(search(&[5, 1, 2, 3, 4], 5), 0);
    }

    #[test]
    fn negative_values() {
        assert_eq!(search(&[0, 1, 2, -3, -2, -1], -3), 3);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 elements rotated so the smallest sits in the middle.
        // The answer is at index 0.
        let mut nums: Vec<i32> = (500..1_000).collect();
        nums.extend(0..500);
        assert_eq!(search(&nums, 500), 0);
    }
}
