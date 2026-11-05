// 150. Evaluate Reverse Polish Notation · Medium · https://leetcode.com/problems/evaluate-reverse-polish-notation/
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
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
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
        check_eq!(Solution::eval_rpn(vec!["2".to_string(), "1".to_string(), "+".to_string(), "3".to_string(), "*".to_string()]), 9);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::eval_rpn(vec!["4".to_string(), "13".to_string(), "5".to_string(), "/".to_string(), "+".to_string()]), 6);
    }

    #[test]
    fn example_3() {
        check_eq!(Solution::eval_rpn(vec!["10".to_string(), "6".to_string(), "9".to_string(), "3".to_string(), "+".to_string(), "-11".to_string(), "*".to_string(), "/".to_string(), "*".to_string(), "17".to_string(), "+".to_string(), "5".to_string(), "+".to_string()]), 22);
    }
}
