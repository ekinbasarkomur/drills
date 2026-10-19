// 1046. Last Stone Weight
// https://leetcode.com/problems/last-stone-weight/
// Plan: Aşama 0 · Heap & Priority Queue
//
// Problem: repeatedly smash the two heaviest stones together. Equal weights
//          destroy each other; otherwise the difference goes back in. Return
//          what is left, or 0.
// Note: You need the two largest values over and over, and the result goes
//       straight back into the pool -- that is a max-heap, not a sort.
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let _ = (stones,);
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {
    println!("{}", Solution::last_stone_weight(vec![2, 3, 6, 2, 4]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn last_stone_weight(stones: &[i32]) -> i32 {
        Solution::last_stone_weight(stones.to_vec())
    }

    #[test]
    fn example_1() {
        assert_eq!(last_stone_weight(&[2, 3, 6, 2, 4]), 1);
    }

    #[test]
    fn example_2() {
        assert_eq!(last_stone_weight(&[1, 2]), 1);
    }

    #[test]
    fn no_stones() {
        assert_eq!(last_stone_weight(&[]), 0);
    }

    #[test]
    fn one_stone_survives_untouched() {
        assert_eq!(last_stone_weight(&[7]), 7);
    }

    #[test]
    fn two_equal_stones_annihilate() {
        assert_eq!(last_stone_weight(&[1, 1]), 0);
    }

    #[test]
    fn two_equal_heavy_stones() {
        assert_eq!(last_stone_weight(&[3, 3]), 0);
    }

    #[test]
    fn the_classic_leetcode_case() {
        assert_eq!(last_stone_weight(&[2, 7, 4, 1, 8, 1]), 1);
    }

    #[test]
    fn a_tie_then_a_leftover() {
        // the two 10s cancel, leaving 4 and 2
        assert_eq!(last_stone_weight(&[10, 4, 2, 10]), 2);
    }

    #[test]
    fn odd_count_of_equal_stones() {
        assert_eq!(last_stone_weight(&[1, 1, 1]), 1);
    }

    #[test]
    fn value_range_extremes() {
        assert_eq!(last_stone_weight(&[1000, 1000, 1000]), 1000);
    }

    #[test]
    fn largest_allowed_input() {
        // 1000 stones of equal weight: they pair off and cancel completely.
        let stones = vec![1000; 1000];
        assert_eq!(last_stone_weight(&stones), 0);
    }
}
