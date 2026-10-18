// 875. Koko Eating Bananas
// https://leetcode.com/problems/koko-eating-bananas/
//
// Problem: find the smallest eating rate k such that every pile is
//          finished within h hours. A pile takes ceil(pile / k) hours, and
//          leftover time in an hour is wasted -- no starting the next pile.
// Note: You are not searching the array, you are searching the ANSWER: every
//       rate from 1 to max(piles) either works or does not, and once one
//       works every larger one does too.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn min_eating_speed(piles: Vec<i32>, h: i32) -> i32 {
        let _ = (piles, h,);
        todo!()
    }
}

fn main() {
    println!("{}", Solution::min_eating_speed(vec![1, 4, 3, 2], 9));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn min_eating_speed(piles: &[i32], h: i32) -> i32 {
        Solution::min_eating_speed(piles.to_vec(), h)
    }

    #[test]
    fn example_1() {
        assert_eq!(min_eating_speed(&[1, 4, 3, 2], 9), 2);
    }

    #[test]
    fn example_2() {
        // h equals the pile count, so each pile must go in one hour
        assert_eq!(min_eating_speed(&[25, 10, 23, 4], 4), 25);
    }

    #[test]
    fn single_pile_single_hour() {
        assert_eq!(min_eating_speed(&[1], 1), 1);
    }

    #[test]
    fn time_to_spare() {
        // k never drops below 1
        assert_eq!(min_eating_speed(&[1], 10), 1);
    }

    #[test]
    fn the_classic_leetcode_case() {
        assert_eq!(min_eating_speed(&[3, 6, 7, 11], 8), 4);
    }

    #[test]
    fn tight_deadline() {
        assert_eq!(min_eating_speed(&[30, 11, 23, 4, 20], 5), 30);
    }

    #[test]
    fn one_hour_more_is_enough_to_slow_down() {
        assert_eq!(min_eating_speed(&[30, 11, 23, 4, 20], 6), 23);
    }

    #[test]
    fn uniform_piles() {
        assert_eq!(min_eating_speed(&[1, 1, 1, 1], 4), 1);
    }

    #[test]
    fn value_range_extremes() {
        // one pile of a billion in one hour -- the rate must match it exactly
        assert_eq!(min_eating_speed(&[1000000000], 1), 1000000000);
    }

    #[test]
    fn largest_allowed_input() {
        // 10_000 piles of 10_000 bananas each and exactly 10_000 hours: one pile
        // per hour, so the rate has to be the pile size. Scanning k from 1
        // upwards would take 10_000 passes; binary search takes 14.
        let piles = vec![10_000; 10_000];
        assert_eq!(min_eating_speed(&piles, 10_000), 10000);
    }
}
