// 271. Encode and Decode Strings
// https://leetcode.com/problems/encode-and-decode-strings/
//
// Problem: turn a list of strings into ONE string, and turn it back. The strings
//          may contain any ASCII character -- including whatever separator you
//          were about to reach for.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn encode(strs: Vec<String>) -> String {
        let mut encoded_string: String = String::new();

        for string in &strs {
            encoded_string = format!("{}{}#{}", encoded_string, string.len(), string);
        }

        encoded_string
    }

    pub fn decode(s: String) -> Vec<String> {
        let mut decoded_vector: Vec<String> = Vec::new();

        let mut rest: String = s;

        while let Some((len, tail)) = rest.split_once("#") {
            let len: usize = len.parse().unwrap();
            let msg = tail[..len].to_string();
            println!("{} - {}", msg, tail);

            decoded_vector.push(msg);

            rest = tail[len..].to_string();
        }

        decoded_vector
    }
}

fn main() {
    let strs = vec!["Hello".to_string(), "World".to_string()];
    let wire = Solution::encode(strs);
    println!("encoded: {:?}", wire);
    println!("decoded: {:?}", Solution::decode(wire));
}

#[cfg(test)]
mod tests {
    use super::*;

    // The encoding format is yours to choose, so the tests never look at the
    // encoded string. They only check that decode(encode(x)) == x.
    fn roundtrip(input: &[&str]) {
        let original: Vec<String> = input.iter().map(|s| s.to_string()).collect();
        let encoded = Solution::encode(original.clone());
        let decoded = Solution::decode(encoded);
        assert_eq!(decoded, original);
    }

    #[test]
    fn example_1() {
        roundtrip(&["Hello", "World"]);
    }

    #[test]
    fn example_2() {
        roundtrip(&[""]);
    }

    #[test]
    fn empty_list() {
        roundtrip(&[]);
    }

    #[test]
    fn several_empty_strings() {
        roundtrip(&["", "", ""]);
    }

    #[test]
    fn empty_string_between_real_ones() {
        roundtrip(&["a", "", "b"]);
    }

    #[test]
    fn single_string() {
        roundtrip(&["lonely"]);
    }

    // The interesting cases: the payload contains whatever you picked as a
    // separator, or text that looks like your own length header.
    #[test]
    fn payload_contains_hash() {
        roundtrip(&["a#b", "#", "##"]);
    }

    #[test]
    fn payload_looks_like_a_length_header() {
        roundtrip(&["3#abc", "12#", "0#"]);
    }

    #[test]
    fn payload_contains_digits_and_punctuation() {
        roundtrip(&["123", ",", ";", "|", ":", "\\"]);
    }

    #[test]
    fn payload_contains_whitespace_and_newlines() {
        roundtrip(&["a b", "\n", "\t\t", " ", "line1\nline2"]);
    }

    #[test]
    fn long_strings_at_the_length_limit() {
        let a = "x".repeat(199);
        let b = "#".repeat(199);
        roundtrip(&[&a, &b]);
    }

    #[test]
    fn many_strings() {
        let items: Vec<String> = (0..99).map(|i| format!("item{i}")).collect();
        let refs: Vec<&str> = items.iter().map(|s| s.as_str()).collect();
        roundtrip(&refs);
    }
}
