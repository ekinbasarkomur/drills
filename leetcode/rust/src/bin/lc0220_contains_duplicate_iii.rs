// 220. Contains Duplicate III · Hard · https://leetcode.com/problems/contains-duplicate-iii/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn contains_nearby_almost_duplicate(nums: Vec<i32>, index_diff: i32, value_diff: i32) -> bool {
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
        check_eq!(Solution::contains_nearby_almost_duplicate(vec![1, 2, 3, 1], 3, 0), true);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::contains_nearby_almost_duplicate(vec![1, 5, 9, 1, 5, 9], 2, 3), false);
    }
}
