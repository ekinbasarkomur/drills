// 1223. Dice Roll Simulation · Hard · https://leetcode.com/problems/dice-roll-simulation/
// Plan: Aşama 4 · Stock Serisi ve DP
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn die_simulator(n: i32, roll_max: Vec<i32>) -> i32 {
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
        assert_eq!(Solution::die_simulator(2, vec![1, 1, 2, 2, 2, 3]), 34);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::die_simulator(2, vec![1, 1, 1, 1, 1, 1]), 30);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::die_simulator(3, vec![1, 1, 1, 2, 2, 3]), 181);
    }
}
