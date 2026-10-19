// 829. Consecutive Numbers Sum · Hard · https://leetcode.com/problems/consecutive-numbers-sum/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn consecutive_numbers_sum(n: i32) -> i32 {
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
        assert_eq!(Solution::consecutive_numbers_sum(5), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::consecutive_numbers_sum(9), 3);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::consecutive_numbers_sum(15), 4);
    }
}
