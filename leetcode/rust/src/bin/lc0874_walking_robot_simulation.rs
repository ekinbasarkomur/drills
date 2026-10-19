// 874. Walking Robot Simulation · Medium · https://leetcode.com/problems/walking-robot-simulation/
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
    pub fn robot_sim(commands: Vec<i32>, obstacles: Vec<Vec<i32>>) -> i32 {
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
        assert_eq!(Solution::robot_sim(vec![4, -1, 3], vec![]), 25);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::robot_sim(vec![4, -1, 4, -2, 4], vec![vec![2, 4]]), 65);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::robot_sim(vec![-1, 9], vec![vec![5, 0], vec![2, 0]]), 36);
    }
}
