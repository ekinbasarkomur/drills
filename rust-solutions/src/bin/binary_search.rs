// 704. Binary Search
// https://leetcode.com/problems/binary-search/
//
// Problem: nums is sorted ascending and every value is distinct. Return the
//          index of target, or -1. Must run in O(log n).
// Note: The classic bug is the loop bound: <= vs <, and whether the midpoint
//       moves. Get those wrong and it either misses the answer or hangs.
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
    println!("{}", Solution::search(vec![-1, 0, 2, 4, 6, 8], 4));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn search(nums: &[i32], target: i32) -> i32 {
        Solution::search(nums.to_vec(), target)
    }

    #[test]
    fn example_1() {
        assert_eq!(search(&[-1, 0, 2, 4, 6, 8], 4), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(search(&[-1, 0, 2, 4, 6, 8], 3), -1);
    }

    #[test]
    fn single_element_found() {
        assert_eq!(search(&[5], 5), 0);
    }

    #[test]
    fn single_element_missing() {
        assert_eq!(search(&[5], 1), -1);
    }

    #[test]
    fn two_elements_first() {
        assert_eq!(search(&[1, 2], 1), 0);
    }

    #[test]
    fn two_elements_second() {
        assert_eq!(search(&[1, 2], 2), 1);
    }

    #[test]
    fn target_at_the_front() {
        assert_eq!(search(&[1, 3, 5, 7, 9], 1), 0);
    }

    #[test]
    fn target_at_the_back() {
        assert_eq!(search(&[1, 3, 5, 7, 9], 9), 4);
    }

    #[test]
    fn below_everything() {
        assert_eq!(search(&[1, 3, 5, 7, 9], 0), -1);
    }

    #[test]
    fn above_everything() {
        assert_eq!(search(&[1, 3, 5, 7, 9], 10), -1);
    }

    #[test]
    fn negative_values() {
        assert_eq!(search(&[-9, -7, -3, -1], -7), 1);
    }

    #[test]
    fn largest_allowed_input() {
        // 10_000 elements, the constraint's ceiling, and the answer is the last
        // one. Binary search finds it in 14 steps; a linear scan takes 10_000.
        let nums: Vec<i32> = (0..10_000).collect();
        assert_eq!(search(&nums, 9_999), 9999);
    }
}
