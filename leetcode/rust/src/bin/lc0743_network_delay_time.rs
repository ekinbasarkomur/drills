// 743. Network Delay Time · Medium · https://leetcode.com/problems/network-delay-time/
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
    pub fn network_delay_time(times: Vec<Vec<i32>>, n: i32, k: i32) -> i32 {
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
        assert_eq!(Solution::network_delay_time(vec![vec![2, 1, 1], vec![2, 3, 1], vec![3, 4, 1]], 4, 2), 2);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::network_delay_time(vec![vec![1, 2, 1]], 2, 1), 1);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::network_delay_time(vec![vec![1, 2, 1]], 2, 2), -1);
    }
}
