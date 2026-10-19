// 342. Power of Four · Easy · https://leetcode.com/problems/power-of-four/
// Plan: Aşama 1 · Bit Manipulation
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn is_power_of_four(n: i32) -> bool {
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
        assert_eq!(Solution::is_power_of_four(16), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::is_power_of_four(5), false);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::is_power_of_four(1), true);
    }
}
