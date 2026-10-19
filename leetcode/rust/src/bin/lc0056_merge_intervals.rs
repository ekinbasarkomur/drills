// 56. Merge Intervals
// https://leetcode.com/problems/merge-intervals/
// Plan: Aşama 0 · Intervals
//
// Problem: merge every pair of intervals that share at least one point, and
//          return the non-overlapping intervals that cover the same ground.
//          Touching counts as overlapping: [1,2] and [2,3] become [1,3].
// Note: the input is NOT sorted, and that is the whole trick -- once it is,
//       one pass is enough because only the previous interval can overlap.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn merge(intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let _ = intervals;
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{:?}", Solution::merge(vec![vec![1, 3], vec![1, 5], vec![6, 7]]));
}

#[cfg(test)]
mod tests {
    use super::*;

    // "You may return the answer in any order" -> sort before comparing.
    fn merge(intervals: &[[i32; 2]]) -> Vec<Vec<i32>> {
        let input = intervals.iter().map(|p| p.to_vec()).collect();
        let mut out = Solution::merge(input);
        out.sort();
        out
    }

    fn expect(intervals: &[[i32; 2]]) -> Vec<Vec<i32>> {
        let mut out: Vec<Vec<i32>> = intervals.iter().map(|p| p.to_vec()).collect();
        out.sort();
        out
    }

    #[test]
    fn example_1() {
        assert_eq!(merge(&[[1, 3], [1, 5], [6, 7]]), expect(&[[1, 5], [6, 7]]));
    }

    #[test]
    fn example_2() {
        // touching at a single point still merges
        assert_eq!(merge(&[[1, 2], [2, 3]]), expect(&[[1, 3]]));
    }

    #[test]
    fn a_single_interval() {
        assert_eq!(merge(&[[1, 4]]), expect(&[[1, 4]]));
    }

    #[test]
    fn nothing_overlaps() {
        assert_eq!(merge(&[[1, 4], [5, 6]]), expect(&[[1, 4], [5, 6]]));
    }

    #[test]
    fn one_interval_swallows_the_rest() {
        assert_eq!(merge(&[[1, 10], [2, 3], [4, 5]]), expect(&[[1, 10]]));
    }

    #[test]
    fn input_arrives_out_of_order() {
        assert_eq!(
            merge(&[[5, 6], [1, 2], [3, 4]]),
            expect(&[[1, 2], [3, 4], [5, 6]])
        );
    }

    #[test]
    fn a_zero_length_interval() {
        assert_eq!(merge(&[[0, 0]]), expect(&[[0, 0]]));
    }

    #[test]
    fn identical_intervals_collapse() {
        assert_eq!(merge(&[[1, 1], [1, 1]]), expect(&[[1, 1]]));
    }

    #[test]
    fn value_range_extremes() {
        assert_eq!(merge(&[[0, 1000]]), expect(&[[0, 1000]]));
    }

    #[test]
    fn a_chain_that_merges_end_to_end() {
        assert_eq!(
            merge(&[[1, 2], [2, 3], [3, 4], [4, 5]]),
            expect(&[[1, 5]])
        );
    }

    #[test]
    fn largest_allowed_input_all_merge() {
        // 1000 intervals all starting at 0: they collapse to one.
        let intervals: Vec<[i32; 2]> = (0..1000).map(|i| [0, i]).collect();
        assert_eq!(merge(&intervals), expect(&[[0, 999]]));
    }

    #[test]
    fn largest_allowed_input_none_merge() {
        // 1000 intervals with a gap between each: nothing collapses.
        let intervals: Vec<[i32; 2]> = (0..500).map(|i| [i * 2, i * 2]).collect();
        assert_eq!(merge(&intervals).len(), 500);
    }
}
