// 1011. Capacity To Ship Packages Within D Days · Medium · https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
// Plan: Aşama 1 · Binary Search
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn ship_within_days(weights: Vec<i32>, days: i32) -> i32 {
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
        check_eq!(Solution::ship_within_days(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::ship_within_days(vec![3, 2, 2, 4, 1, 4], 3), 6);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::ship_within_days(vec![1, 2, 3, 1, 1], 4), 3);
    }
}
