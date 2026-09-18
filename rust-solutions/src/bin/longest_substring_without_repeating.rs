// 3. Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/
//
// Problem: length of the longest contiguous stretch of s in which no
//          character repeats. s may contain any printable ASCII.
// Note: A window that only ever grows from the right and shrinks from the
//       left visits each character twice at most.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let _ = (s,);
        todo!()
    }
}

fn main() {
    println!("{}", Solution::length_of_longest_substring("zxyzxyz".into()));
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
