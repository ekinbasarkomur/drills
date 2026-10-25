// 20. Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/
// Plan: Aşama 0 · Stack
//
// Problem: every bracket closed by its own kind, in the right order,
//          and nothing left open at the end.
// Note: The most recently opened bracket is the first that has to close --
//       that is exactly what a stack gives you.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut expected: Vec<char> = Vec::new();

        for c in s.chars() {
            match c {
                '(' => expected.push(')'),
                '{' => expected.push('}'),
                '[' => expected.push(']'),
                _ => match expected.pop() {
                    Some(expected_c) if expected_c == c => {}
                    _ => return false,
                },
            }
        }

        expected.is_empty()

    }

}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::is_valid("[]".into()));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn is_valid(s: &str) -> bool {
        Solution::is_valid(s.to_string())
    }

    #[test]
    fn example_1() {
        assert_eq!(is_valid("[]"), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(is_valid("([{}])"), true);
    }

    #[test]
    fn example_3() {
        // right counts, wrong order
        assert_eq!(is_valid("[(])"), false);
    }

    #[test]
    fn empty_string() {
        // nothing left open
        assert_eq!(is_valid(""), true);
    }

    #[test]
    fn one_opening_bracket() {
        assert_eq!(is_valid("("), false);
    }

    #[test]
    fn one_closing_bracket() {
        assert_eq!(is_valid(")"), false);
    }

    #[test]
    fn all_three_kinds_side_by_side() {
        assert_eq!(is_valid("()[]{}"), true);
    }

    #[test]
    fn mismatched_pair() {
        assert_eq!(is_valid("(]"), false);
    }

    #[test]
    fn a_wrong_closer_is_not_skipped() {
        // the ']' must fail immediately; ignoring it lets ')' close the '('
        assert_eq!(is_valid("(])"), false);
    }

    #[test]
    fn only_openers() {
        assert_eq!(is_valid("(((("), false);
    }

    #[test]
    fn only_closers() {
        assert_eq!(is_valid("))))"), false);
    }

    #[test]
    fn deeply_nested() {
        assert_eq!(is_valid("{[()]}"), true);
    }

    #[test]
    fn one_opener_left_over() {
        assert_eq!(is_valid("(()"), false);
    }

    #[test]
    fn one_closer_too_many() {
        assert_eq!(is_valid("())"), false);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 brackets: 500 openers then 500 closers, the constraint's ceiling.
        let s = "(".repeat(500) + &")".repeat(500);
        assert_eq!(is_valid(&s), true);
    }
}
