// 347. Top K Frequent Elements https://leetcode.com/problems/top-k-frequent-elements/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return the k most frequent values in nums. The answer is unique and
//          may be returned in any order.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut inventory: HashMap<i32, i32> = HashMap::new();

        for num in nums {
            inventory.entry(num).and_modify(|e| *e += 1).or_insert(1);
        }

        let mut pairs: Vec<(i32, i32)> = inventory.into_iter().collect();

        pairs.sort_by(|a, b| b.1.cmp(&a.1));

        pairs
            .into_iter()
            .take(k as usize)
            .map(|pair| pair.0)
            .collect()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::top_k_frequent(vec![1, 2, 2, 3, 3, 3], 2));
    println!("{:?}", Solution::top_k_frequent(vec![7, 7], 1));
}

#[cfg(test)]
mod tests {
    use super::*;

    // "You may return the output in any order" -> sort before comparing.
    fn top_k(nums: &[i32], k: i32) -> Vec<i32> {
        let mut out = Solution::top_k_frequent(nums.to_vec(), k);
        out.sort();
        out
    }

    fn expect(vals: &[i32]) -> Vec<i32> {
        let mut v = vals.to_vec();
        v.sort();
        v
    }

    #[test]
    fn example_1() {
        assert_eq!(top_k(&[1, 2, 2, 3, 3, 3], 2), expect(&[2, 3]));
    }

    #[test]
    fn example_2() {
        assert_eq!(top_k(&[7, 7], 1), expect(&[7]));
    }

    #[test]
    fn single_element() {
        assert_eq!(top_k(&[1], 1), expect(&[1]));
    }

    #[test]
    fn k_equals_number_of_distinct_values() {
        assert_eq!(top_k(&[1, 1, 2, 2, 3], 3), expect(&[1, 2, 3]));
    }

    #[test]
    fn negative_values() {
        assert_eq!(top_k(&[-1, -1, -1, -2, -2, 5], 2), expect(&[-1, -2]));
    }

    #[test]
    fn extremes_of_the_value_range() {
        assert_eq!(
            top_k(&[1000, 1000, -1000, -1000, -1000, 7], 1),
            expect(&[-1000])
        );
    }

    #[test]
    fn least_frequent_values_are_excluded() {
        assert_eq!(top_k(&[4, 4, 4, 4, 9, 9, 9, 1, 1, 6], 2), expect(&[4, 9]));
    }

    #[test]
    fn every_value_appears_once_except_one() {
        assert_eq!(top_k(&[5, 6, 7, 8, 8], 1), expect(&[8]));
    }
}
