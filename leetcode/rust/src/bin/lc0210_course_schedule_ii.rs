// 210. Course Schedule II · Medium · https://leetcode.com/problems/course-schedule-ii/
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
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![0, 1];
        check_eq!(Solution::find_order(2, vec![vec![1, 0]]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![0, 2, 1, 3];
        check_eq!(Solution::find_order(4, vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]]), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![0];
        check_eq!(Solution::find_order(1, vec![]), want);
    }
}
