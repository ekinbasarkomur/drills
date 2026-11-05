// 238. Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: output[i] is the product of every element of nums except nums[i].
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut prefix: Vec<i32> = vec![1];
        let mut suffix: Vec<i32> = vec![1];
        let mut output: Vec<i32> = Vec::new();
        let len = nums.len();

        for (i, &num) in nums.iter().enumerate() {
            prefix.push(prefix[i] * num);
            suffix.push(suffix[i] * nums[len - i - 1]);
        }

        for i in 0..len {
            //println!("{} - {}", prefix[i], suffix[i]);
            output.push(prefix[i] * suffix[len - i - 1]);
        }

        output
    }

}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::product_except_self(vec![1, 2, 4, 6]));
    println!("{:?}", Solution::product_except_self(vec![-1, 0, 1, 2, 3]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn product(nums: &[i32]) -> Vec<i32> {
        Solution::product_except_self(nums.to_vec())
    }

    #[test]
    fn example_1() {
        check_eq!(product(&[1, 2, 4, 6]), vec![48, 24, 12, 8]);
    }

    #[test]
    fn example_2() {
        check_eq!(product(&[-1, 0, 1, 2, 3]), vec![0, -6, 0, 0, 0]);
    }

    #[test]
    fn shortest_possible_input() {
        check_eq!(product(&[2, 3]), vec![3, 2]);
    }

    #[test]
    fn all_ones() {
        check_eq!(product(&[1, 1, 1, 1]), vec![1, 1, 1, 1]);
    }

    // The two cases a naive "divide by nums[i]" solution gets wrong.
    #[test]
    fn one_zero_in_the_middle() {
        check_eq!(product(&[1, 2, 0, 4]), vec![0, 0, 8, 0]);
    }

    #[test]
    fn two_zeros_make_everything_zero() {
        check_eq!(product(&[0, 4, 0, 5]), vec![0, 0, 0, 0]);
    }

    #[test]
    fn zero_at_each_end() {
        check_eq!(product(&[0, 3, 5]), vec![15, 0, 0]);
        check_eq!(product(&[3, 5, 0]), vec![0, 0, 15]);
    }

    #[test]
    fn negative_numbers_flip_the_sign() {
        check_eq!(product(&[-1, -2, -3]), vec![6, 3, 2]);
        check_eq!(product(&[-2, 3, -4]), vec![-12, 8, -6]);
    }

    #[test]
    fn value_range_extremes() {
        check_eq!(product(&[-30, 30]), vec![30, -30]);
    }

    // 100_000 elements: anything O(n^2) will hang here rather than fail.
    #[test]
    fn large_input_stays_linear() {
        let n = 100_000;
        let mut nums = vec![1; n];
        nums[7] = 0;

        let out = product(&nums);

        // Every position except index 7 multiplies through that zero.
        check_eq!(out.len(), n);
        check_eq!(out[7], 1);
        check!(
            out.iter()
                .enumerate()
                .all(|(i, &v)| v == if i == 7 { 1 } else { 0 })
        );
    }
}
