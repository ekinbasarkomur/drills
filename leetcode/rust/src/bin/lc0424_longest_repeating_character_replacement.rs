// 424. Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/
// Plan: Aşama 0 · Sliding Window
//
// Problem: after replacing at most k characters of s with any uppercase
//          letter, how long can a run of one single letter get?
// Note: A window is usable when (its length - the count of its most common
//       letter) <= k: that difference is how many replacements it costs.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let _ = (s, k,);
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::character_replacement("XYYX".into(), 2));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn character_replacement(s: &str, k: i32) -> i32 {
        Solution::character_replacement(s.to_string(), k)
    }

    #[test]
    fn example_1() {
        // replace both X's with Y's, or the other way round
        check_eq!(character_replacement("XYYX", 2), 4);
    }

    #[test]
    fn example_2() {
        check_eq!(character_replacement("AAABABB", 1), 5);
    }

    #[test]
    fn single_character_no_budget() {
        check_eq!(character_replacement("A", 0), 1);
    }

    #[test]
    fn single_character_with_budget() {
        // k can exceed what is useful
        check_eq!(character_replacement("A", 1), 1);
    }

    #[test]
    fn two_letters_no_budget() {
        check_eq!(character_replacement("AB", 0), 1);
    }

    #[test]
    fn two_letters_one_replacement() {
        check_eq!(character_replacement("AB", 1), 2);
    }

    #[test]
    fn already_uniform() {
        // nothing to replace
        check_eq!(character_replacement("BBBB", 0), 4);
    }

    #[test]
    fn all_distinct_no_budget() {
        check_eq!(character_replacement("ABCDE", 0), 1);
    }

    #[test]
    fn all_distinct_budget_covers_everything() {
        check_eq!(character_replacement("ABCDE", 4), 5);
    }

    #[test]
    fn budget_larger_than_needed() {
        check_eq!(character_replacement("AAAA", 2), 4);
    }

    #[test]
    fn one_odd_letter_at_the_front() {
        check_eq!(character_replacement("ABBB", 0), 3);
    }

    #[test]
    fn the_window_must_shrink() {
        check_eq!(character_replacement("AABABBA", 1), 4);
    }

    #[test]
    fn alternating_letters() {
        check_eq!(character_replacement("ABAB", 2), 4);
    }

    #[test]
    fn largest_allowed_input() {
        // 100_000 A's and k = 0: the whole string already qualifies.
        // An O(n^2) solution will hang here rather than fail.
        let s = "A".repeat(100_000);
        check_eq!(character_replacement(&s, 0), 100000);
    }
}
