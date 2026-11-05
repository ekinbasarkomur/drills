// 68. Text Justification · Hard · https://leetcode.com/problems/text-justification/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn full_justify(words: Vec<String>, max_width: i32) -> Vec<String> {
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
        let want: Vec<String> = vec!["This    is    an".to_string(), "example  of text".to_string(), "justification.  ".to_string()];
        check_eq!(Solution::full_justify(vec!["This".to_string(), "is".to_string(), "an".to_string(), "example".to_string(), "of".to_string(), "text".to_string(), "justification.".to_string()], 16), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<String> = vec!["What   must   be".to_string(), "acknowledgment  ".to_string(), "shall be        ".to_string()];
        check_eq!(Solution::full_justify(vec!["What".to_string(), "must".to_string(), "be".to_string(), "acknowledgment".to_string(), "shall".to_string(), "be".to_string()], 16), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<String> = vec!["Science  is  what we".to_string(), "understand      well".to_string(), "enough to explain to".to_string(), "a  computer.  Art is".to_string(), "everything  else  we".to_string(), "do                  ".to_string()];
        check_eq!(Solution::full_justify(vec!["Science".to_string(), "is".to_string(), "what".to_string(), "we".to_string(), "understand".to_string(), "well".to_string(), "enough".to_string(), "to".to_string(), "explain".to_string(), "to".to_string(), "a".to_string(), "computer.".to_string(), "Art".to_string(), "is".to_string(), "everything".to_string(), "else".to_string(), "we".to_string(), "do".to_string()], 20), want);
    }
}
