// 332. Reconstruct Itinerary · Hard · https://leetcode.com/problems/reconstruct-itinerary/
// Plan: Aşama 4 · Graph
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn find_itinerary(tickets: Vec<Vec<String>>) -> Vec<String> {
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
        let want: Vec<String> = vec!["JFK".to_string(), "MUC".to_string(), "LHR".to_string(), "SFO".to_string(), "SJC".to_string()];
        assert_eq!(Solution::find_itinerary(vec![vec!["MUC".to_string(), "LHR".to_string()], vec!["JFK".to_string(), "MUC".to_string()], vec!["SFO".to_string(), "SJC".to_string()], vec!["LHR".to_string(), "SFO".to_string()]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<String> = vec!["JFK".to_string(), "ATL".to_string(), "JFK".to_string(), "SFO".to_string(), "ATL".to_string(), "SFO".to_string()];
        assert_eq!(Solution::find_itinerary(vec![vec!["JFK".to_string(), "SFO".to_string()], vec!["JFK".to_string(), "ATL".to_string()], vec!["SFO".to_string(), "ATL".to_string()], vec!["ATL".to_string(), "JFK".to_string()], vec!["ATL".to_string(), "SFO".to_string()]]), want);
    }
}
