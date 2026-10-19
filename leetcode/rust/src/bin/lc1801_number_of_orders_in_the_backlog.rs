// 1801. Number of Orders in the Backlog · Medium · https://leetcode.com/problems/number-of-orders-in-the-backlog/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn get_number_of_backlog_orders(orders: Vec<Vec<i32>>) -> i32 {
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
        assert_eq!(Solution::get_number_of_backlog_orders(vec![vec![10, 5, 0], vec![15, 2, 1], vec![25, 1, 1], vec![30, 4, 0]]), 6);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::get_number_of_backlog_orders(vec![vec![7, 1000000000, 1], vec![15, 3, 0], vec![5, 999999995, 0], vec![5, 1, 1]]), 999999984);
    }
}
