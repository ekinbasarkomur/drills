// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
// Plan: Aşama 0 · Sliding Window
//
// Problem: length of the longest contiguous stretch of s in which no
//          character repeats. s may contain any printable ASCII.
// Note: A window that only ever grows from the right and shrinks from the
//       left visits each character twice at most.
// Approach: sliding window with a last-seen index per character. `right` adds one
//           character per step; if that character was last seen inside the window,
//           `left` jumps straight past that position (no inner loop).
// Time O(n), space O(1) -- a fixed 256-entry array

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let mut last: Vec<i32> = Vec::new();
        last.resize(256, -1);

        let mut longest_streak: i32 = 0;
        let mut left: i32 = 0;

        for (right, c) in s.chars().enumerate() {
            if last[c as usize] >= left {
                left = last[c as usize] + 1;
            }

            last[c as usize] = right as i32;
            longest_streak = std::cmp::max(longest_streak, right as i32 - left + 1);
        }
        longest_streak
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!(
        "{}",
        Solution::length_of_longest_substring("zxyzxyz".into())
    );
}

#[cfg(test)]
mod tests {
    use super::*;

    fn length_of_longest_substring(s: &str) -> i32 {
        Solution::length_of_longest_substring(s.to_string())
    }

    #[test]
    fn example_1() {
        assert_eq!(length_of_longest_substring("zxyzxyz"), 3);
    }

    #[test]
    fn example_2() {
        assert_eq!(length_of_longest_substring("xxxx"), 1);
    }

    #[test]
    fn empty_string() {
        assert_eq!(length_of_longest_substring(""), 0);
    }

    #[test]
    fn single_character() {
        assert_eq!(length_of_longest_substring("a"), 1);
    }

    #[test]
    fn two_distinct_characters() {
        assert_eq!(length_of_longest_substring("ab"), 2);
    }

    #[test]
    fn every_character_is_the_same() {
        assert_eq!(length_of_longest_substring("bbbbb"), 1);
    }

    #[test]
    fn the_classic_leetcode_case() {
        assert_eq!(length_of_longest_substring("abcabcbb"), 3);
    }

    #[test]
    fn the_answer_is_not_a_prefix() {
        // \"wke\", not \"pwe\" -- the answer must be contiguous
        assert_eq!(length_of_longest_substring("pwwkew"), 3);
    }

    #[test]
    fn a_repeat_before_the_window_start() {
        // after 'a' repeats the window must not jump back behind the second 'b'
        assert_eq!(length_of_longest_substring("abba"), 2);
    }

    #[test]
    fn stale_index_must_be_ignored() {
        // \"mzuxt\"
        assert_eq!(length_of_longest_substring("tmmzuxt"), 5);
    }

    #[test]
    fn a_repeat_keeps_the_characters_after_it() {
        // at the second 'a' the window becomes "bca", not "a"
        assert_eq!(length_of_longest_substring("abcad"), 4);
    }

    #[test]
    fn the_answer_spans_the_repeated_character() {
        // "vdf": the second 'd' only evicts the first 'd', 'v' stays
        assert_eq!(length_of_longest_substring("dvdf"), 3);
    }

    #[test]
    fn spaces_count_as_characters() {
        assert_eq!(length_of_longest_substring("a b c"), 3);
    }

    #[test]
    fn punctuation_and_symbols() {
        assert_eq!(length_of_longest_substring(" !@# !@#"), 4);
    }

    #[test]
    fn largest_allowed_input() {
        // 50_000 characters cycling through the 95 printable ASCII codes, so the
        // answer is one full cycle. An O(n^2) solution will hang here.
        let s: String = (0..50_000).map(|i| (32 + (i % 95) as u8) as char).collect();
        assert_eq!(length_of_longest_substring(&s), 95);
    }
}
