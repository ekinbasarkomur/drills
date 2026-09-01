// 125. Valid Palindrome        https://leetcode.com/problems/valid-palindrome/
//
// Problem: is s a palindrome, ignoring case and every non-alphanumeric
//          character? Input is printable ASCII.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let _ = s;
        todo!()
    }
}

fn main() {
    println!("{}", Solution::is_palindrome("Was it a car or a cat I saw?".into()));
    println!("{}", Solution::is_palindrome("tab a cat".into()));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn palindrome(s: &str) -> bool {
        Solution::is_palindrome(s.to_string())
    }

    #[test]
    fn example_1() {
        assert!(palindrome("Was it a car or a cat I saw?"));
    }

    #[test]
    fn example_2() {
        assert!(!palindrome("tab a cat"));
    }

    #[test]
    fn single_character() {
        assert!(palindrome("a"));
    }

    #[test]
    fn two_identical_characters() {
        assert!(palindrome("aa"));
    }

    #[test]
    fn two_different_characters() {
        assert!(!palindrome("ab"));
    }

    #[test]
    fn nothing_alphanumeric_at_all() {
        // everything is stripped, an empty string is a palindrome
        assert!(palindrome(".,!?"));
        assert!(palindrome(" "));
    }

    #[test]
    fn punctuation_between_the_letters() {
        assert!(palindrome("A man, a plan, a canal: Panama"));
    }

    #[test]
    fn digits_count_as_alphanumeric() {
        assert!(palindrome("12321"));
        assert!(!palindrome("12345"));
    }

    #[test]
    fn letters_and_digits_together() {
        assert!(palindrome("1a2a1"));
    }

    #[test]
    fn digit_against_letter_is_not_equal() {
        // the classic trap: '0' and 'P' are 32 apart in ASCII, like 'a' and 'A'
        assert!(!palindrome("0P"));
    }

    #[test]
    fn case_is_ignored() {
        assert!(palindrome("Aa"));
        assert!(palindrome("RaceCar"));
    }

    #[test]
    fn odd_length_ignores_the_middle_character() {
        assert!(palindrome("aba"));
        assert!(palindrome("abXba"));
    }

    #[test]
    fn even_length_has_no_free_middle() {
        assert!(palindrome("abba"));
        assert!(!palindrome("abca"));
    }

    #[test]
    fn difference_only_at_the_very_ends() {
        assert!(!palindrome("abcdefghijklmnopqrstuvwxyZ"));
    }

    #[test]
    fn long_palindrome_at_the_length_limit() {
        let half = "abcde".repeat(100); // 500 chars
        let reversed: String = half.chars().rev().collect();
        assert!(palindrome(&(half + &reversed)));
    }
}
