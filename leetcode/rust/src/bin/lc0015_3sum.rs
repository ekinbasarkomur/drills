// 15. 3Sum
// https://leetcode.com/problems/3sum/
// Plan: Aşama 0 · Two Pointers
//
// Problem: every triplet of distinct indices summing to zero, with no duplicate
//          triplets in the output. Order does not matter.
// Note: the hard part is not finding the triplets, it is not emitting the same
//       one twice -- [-1,0,1] can be built from several index combinations.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::cmp::Ordering;

impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut output: Vec<Vec<i32>> = vec![];
        let mut sorted_nums = nums;
        sorted_nums.sort();

        for i in 0..sorted_nums.len() - 2 {
            if i > 0 && sorted_nums[i] == sorted_nums[i - 1] {
                continue;
            }

            let target = -sorted_nums[i];
            let mut left = i + 1;
            let mut right = sorted_nums.len() - 1;

            while left < right {
                let sum = sorted_nums[left] + sorted_nums[right];


                match sum.cmp(&target) {
                    Ordering::Less => left += 1,
                    Ordering::Greater => right -= 1,
                    Ordering::Equal => {
                        output.push(vec![sorted_nums[i], sorted_nums[left], sorted_nums[right]]);

                        left += 1;
                        right -= 1;

                        while left < right && sorted_nums[left] == sorted_nums[left - 1] {
                            left += 1;
                        }
                        while left < right && sorted_nums[right] == sorted_nums[right + 1] {
                            right -= 1;
                        }

                    }

                }
            }
        }

        return output;
    }

}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::three_sum(vec![-1, 0, 1, 2, -1, -4]));
}

#[cfg(test)]
mod tests {
    use super::*;

    // "You may return the output and the triplets in any order" -> sort both
    // levels before comparing.
    fn three_sum(nums: &[i32]) -> Vec<Vec<i32>> {
        let mut out = Solution::three_sum(nums.to_vec());
        for t in out.iter_mut() {
            t.sort();
        }
        out.sort();
        out
    }

    fn expect(triplets: &[[i32; 3]]) -> Vec<Vec<i32>> {
        let mut out: Vec<Vec<i32>> = triplets
            .iter()
            .map(|t| {
                let mut t = t.to_vec();
                t.sort();
                t
            })
            .collect();
        out.sort();
        out
    }

    #[test]
    fn example_1() {
        assert_eq!(
            three_sum(&[-1, 0, 1, 2, -1, -4]),
            expect(&[[-1, -1, 2], [-1, 0, 1]])
        );
    }

    #[test]
    fn example_2() {
        assert_eq!(three_sum(&[0, 1, 1]), expect(&[]));
    }

    #[test]
    fn example_3() {
        assert_eq!(three_sum(&[0, 0, 0]), expect(&[[0, 0, 0]]));
    }

    #[test]
    fn all_positive_cannot_reach_zero() {
        assert_eq!(three_sum(&[1, 2, 3]), expect(&[]));
    }

    #[test]
    fn all_negative_cannot_reach_zero() {
        assert_eq!(three_sum(&[-1, -2, -3]), expect(&[]));
    }

    // Duplicate handling: the same triplet must appear exactly once.

    #[test]
    fn four_zeros_yield_one_triplet() {
        assert_eq!(three_sum(&[0, 0, 0, 0]), expect(&[[0, 0, 0]]));
    }

    #[test]
    fn a_repeated_value_inside_a_triplet() {
        assert_eq!(
            three_sum(&[-2, 0, 1, 1, 2]),
            expect(&[[-2, 0, 2], [-2, 1, 1]])
        );
    }

    #[test]
    fn many_repeats_many_triplets() {
        assert_eq!(
            three_sum(&[-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]),
            expect(&[
                [-4, -2, 6],
                [-4, 0, 4],
                [-4, 1, 3],
                [-4, 2, 2],
                [-2, -2, 4],
                [-2, 0, 2],
            ])
        );
    }

    #[test]
    fn same_values_different_order_in_the_input() {
        assert_eq!(
            three_sum(&[1, -1, 0, 2, -2, 0]),
            expect(&[[-2, 0, 2], [-1, 0, 1]])
        );
    }

    #[test]
    fn value_range_extremes() {
        assert_eq!(
            three_sum(&[100_000, -100_000, 0]),
            expect(&[[-100_000, 0, 100_000]])
        );
        assert_eq!(
            three_sum(&[-100_000, 50_000, 50_000]),
            expect(&[[-100_000, 50_000, 50_000]])
        );
    }

    #[test]
    fn largest_allowed_input() {
        // 3000 elements, all 1 except three that form the only triplet.
        // An O(n^3) solution will hang here rather than fail.
        let mut nums = vec![1; 2997];
        nums.extend([-5, 2, 3]);
        assert_eq!(three_sum(&nums), expect(&[[-5, 2, 3]]));
    }
}
