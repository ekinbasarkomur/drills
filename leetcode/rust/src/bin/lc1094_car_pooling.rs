// 1094. Car Pooling · Medium · https://leetcode.com/problems/car-pooling/
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
    pub fn car_pooling(trips: Vec<Vec<i32>>, capacity: i32) -> bool {
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
        check_eq!(Solution::car_pooling(vec![vec![2, 1, 5], vec![3, 3, 7]], 4), false);
    }

    #[test]
    fn example_2() {
        check_eq!(Solution::car_pooling(vec![vec![2, 1, 5], vec![3, 3, 7]], 5), true);
    }
}
