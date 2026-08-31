// 49. Group Anagrams           https://leetcode.com/problems/group-anagrams/
//
// Problem: bucket the input strings so that anagrams end up in the same sublist.
// Approach: two words are anagrams exactly when their sorted letters match, so
//           the sorted string is a canonical key. Group by it in a HashMap and
//           hand back the values.
//           Time O(n * k log k) for n words of length k, space O(n * k).

use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {

        let mut sorted_strings: HashMap<String, Vec<String>> = HashMap::new();

        for string in strs
        {
            let mut chars : Vec<char> = string.chars().collect();
            chars.sort_unstable();
            let sorted_string: String = chars.into_iter().collect();
            sorted_strings.entry(sorted_string).or_default().push(string);

        }

        sorted_strings.into_values().collect()
    }
}

fn main() {
    let input = ["act", "pots", "tops", "cat", "stop", "hat"];
    let out = Solution::group_anagrams(input.iter().map(|s| s.to_string()).collect());
    println!("{:?}", out);
}

#[cfg(test)]
mod tests {
    use super::*;

    // The problem says the output may come back in any order, and HashMap
    // iteration order is random anyway (NOTES §92). So sort both the inner
    // lists and the outer list before comparing.
    fn grouped(input: &[&str]) -> Vec<Vec<String>> {
        let mut out = Solution::group_anagrams(
            input.iter().map(|s| s.to_string()).collect(),
        );
        for group in out.iter_mut() {
            group.sort();
        }
        out.sort();
        out
    }

    fn expect(groups: &[&[&str]]) -> Vec<Vec<String>> {
        let mut out: Vec<Vec<String>> = groups
            .iter()
            .map(|g| {
                let mut g: Vec<String> = g.iter().map(|s| s.to_string()).collect();
                g.sort();
                g
            })
            .collect();
        out.sort();
        out
    }

    #[test]
    fn example_1() {
        assert_eq!(
            grouped(&["act", "pots", "tops", "cat", "stop", "hat"]),
            expect(&[&["hat"], &["act", "cat"], &["stop", "pots", "tops"]])
        );
    }

    #[test]
    fn example_2() {
        assert_eq!(grouped(&["x"]), expect(&[&["x"]]));
    }

    #[test]
    fn example_3() {
        assert_eq!(grouped(&[""]), expect(&[&[""]]));
    }

    #[test]
    fn no_two_words_are_anagrams() {
        assert_eq!(
            grouped(&["abc", "de", "f"]),
            expect(&[&["abc"], &["de"], &["f"]])
        );
    }

    #[test]
    fn everything_in_one_group() {
        assert_eq!(
            grouped(&["abc", "bca", "cab"]),
            expect(&[&["abc", "bca", "cab"]])
        );
    }

    #[test]
    fn duplicates_stay_as_separate_entries() {
        assert_eq!(
            grouped(&["ab", "ab", "ba"]),
            expect(&[&["ab", "ab", "ba"]])
        );
    }

    #[test]
    fn repeated_letters_are_not_confused() {
        // same letter set, different counts -> different groups
        assert_eq!(
            grouped(&["aab", "abb"]),
            expect(&[&["aab"], &["abb"]])
        );
    }

    #[test]
    fn several_empty_strings_group_together() {
        assert_eq!(grouped(&["", "", "a"]), expect(&[&["", ""], &["a"]]));
    }
}
