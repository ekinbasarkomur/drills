// 253. Meeting Rooms II · Medium · https://leetcode.com/problems/meeting-rooms-ii/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn min_meeting_rooms(intervals: Vec<Vec<i32>>) -> i32 {
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
        // Premium problem: the expected output is not public, so this only runs it.
        Solution::min_meeting_rooms(vec![vec![0, 30], vec![5, 10], vec![15, 20]]);
    }

    #[test]
    fn example_2() {
        // Premium problem: the expected output is not public, so this only runs it.
        Solution::min_meeting_rooms(vec![vec![7, 10], vec![2, 4]]);
    }
}
