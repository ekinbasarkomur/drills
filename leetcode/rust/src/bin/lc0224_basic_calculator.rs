// 224. Basic Calculator · Hard · https://leetcode.com/problems/basic-calculator/
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
    pub fn calculate(s: String) -> i32 {
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
        assert_eq!(Solution::calculate("1 + 1".to_string()), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::calculate(" 2-1 + 2 ".to_string()), 3);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::calculate("(1+(4+5+2)-3)+(6+8)".to_string()), 23);
    }
}
