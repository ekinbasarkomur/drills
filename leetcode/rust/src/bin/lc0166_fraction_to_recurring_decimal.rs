// 166. Fraction to Recurring Decimal · Medium · https://leetcode.com/problems/fraction-to-recurring-decimal/
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
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
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
        let want: String = "0.5".to_string();
        assert_eq!(Solution::fraction_to_decimal(1, 2), want);
    }

    #[test]
    fn example_2() {
        let want: String = "2".to_string();
        assert_eq!(Solution::fraction_to_decimal(2, 1), want);
    }

    #[test]
    fn example_3() {
        let want: String = "0.(012)".to_string();
        assert_eq!(Solution::fraction_to_decimal(4, 333), want);
    }
}
