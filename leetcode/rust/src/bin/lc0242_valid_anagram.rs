// 242. Valid Anagram           https://leetcode.com/problems/valid-anagram/
// Plan: Aşama 0 · Arrays & Hashing
//
// Problem: return true if t is a rearrangement of s.
// Approach: lengths must match first. Then count how often each char occurs in
//           each string and compare the two count maps. zip() works here only
//           because the lengths are already known to be equal.
//           Time O(n), space O(n).

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
use std::collections::HashMap;

impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {

        if s.len() != t.len()
        {
            return false;
        }

        let mut s_map: HashMap<char, i32> = HashMap::new();
        let mut t_map: HashMap<char, i32> = HashMap::new();

        for (s_char, t_char) in s.chars().zip(t.chars())
        {
            *s_map.entry(s_char).or_insert(0) += 1;
            *t_map.entry(t_char).or_insert(0) += 1;
        }

        s_map == t_map
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::is_anagram("racecar".into(), "carrace".into()));
    println!("{}", Solution::is_anagram("jar".into(), "jam".into()));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn is_anagram(s: &str, t: &str) -> bool {
        Solution::is_anagram(s.to_string(), t.to_string())
    }

    #[test]
    fn example_1() {
        assert!(is_anagram("racecar", "carrace"));
    }

    #[test]
    fn example_2() {
        assert!(!is_anagram("jar", "jam"));
    }

    #[test]
    fn example_3() {
        assert!(is_anagram("x", "x"));
    }

    #[test]
    fn different_lengths() {
        assert!(!is_anagram("ab", "abc"));
    }

    #[test]
    fn same_letters_different_counts() {
        assert!(!is_anagram("aab", "abb"));
    }

    #[test]
    fn identical_strings() {
        assert!(is_anagram("anagram", "anagram"));
    }

    #[test]
    fn no_letters_in_common() {
        assert!(!is_anagram("abc", "xyz"));
    }
}
