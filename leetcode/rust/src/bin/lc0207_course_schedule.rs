// 207. Course Schedule · Medium · https://leetcode.com/problems/course-schedule/
// Plan: Aşama 0 · Graphs
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
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
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0]]), true);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::can_finish(2, vec![vec![1, 0], vec![0, 1]]), false);
    }
}
