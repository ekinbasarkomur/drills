// 787. Cheapest Flights Within K Stops · Medium · https://leetcode.com/problems/cheapest-flights-within-k-stops/
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
    pub fn find_cheapest_price(n: i32, flights: Vec<Vec<i32>>, src: i32, dst: i32, k: i32) -> i32 {
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
        assert_eq!(Solution::find_cheapest_price(4, vec![vec![0, 1, 100], vec![1, 2, 100], vec![2, 0, 100], vec![1, 3, 600], vec![2, 3, 200]], 0, 3, 1), 700);
    }

    #[test]
    fn example_2() {
        assert_eq!(Solution::find_cheapest_price(3, vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]], 0, 2, 1), 200);
    }

    #[test]
    fn example_3() {
        assert_eq!(Solution::find_cheapest_price(3, vec![vec![0, 1, 100], vec![1, 2, 100], vec![0, 2, 500]], 0, 2, 0), 500);
    }
}
