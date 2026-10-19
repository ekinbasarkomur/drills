// 315. Count of Smaller Numbers After Self · Hard · https://leetcode.com/problems/count-of-smaller-numbers-after-self/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn count_smaller(nums: Vec<i32>) -> Vec<i32> {
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
        let want: Vec<i32> = vec![2, 1, 1, 0];
        assert_eq!(Solution::count_smaller(vec![5, 2, 6, 1]), want);
    }

    #[test]
    fn example_2() {
        let want: Vec<i32> = vec![0];
        assert_eq!(Solution::count_smaller(vec![-1]), want);
    }

    #[test]
    fn example_3() {
        let want: Vec<i32> = vec![0, 0];
        assert_eq!(Solution::count_smaller(vec![-1, -1]), want);
    }
}
