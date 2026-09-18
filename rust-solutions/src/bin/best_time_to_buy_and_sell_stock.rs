// 121. Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
//
// Problem: buy on one day and sell on a LATER day. Return the best profit,
//          or 0 if every later price is lower.
// Note: You never need to look ahead: the best sale on day i is against the
//       cheapest price seen so far, so one pass is enough.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let _ = (prices,);
        todo!()
    }
}

fn main() {
    println!("{}", Solution::max_profit(vec![10, 1, 5, 6, 7, 1]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn max_profit(prices: &[i32]) -> i32 {
        Solution::max_profit(prices.to_vec())
    }

    #[test]
    fn example_1() {
        assert_eq!(max_profit(&[10, 1, 5, 6, 7, 1]), 6);
    }

    #[test]
    fn example_2() {
        // prices only fall, so no transaction is made
        assert_eq!(max_profit(&[10, 8, 7, 5, 2]), 0);
    }

    #[test]
    fn single_day() {
        // nothing to sell into
        assert_eq!(max_profit(&[1]), 0);
    }

    #[test]
    fn two_days_rising() {
        assert_eq!(max_profit(&[1, 2]), 1);
    }

    #[test]
    fn two_days_falling() {
        assert_eq!(max_profit(&[2, 1]), 0);
    }

    #[test]
    fn flat_prices() {
        assert_eq!(max_profit(&[5, 5, 5]), 0);
    }

    #[test]
    fn all_zeros() {
        assert_eq!(max_profit(&[0, 0, 0]), 0);
    }

    #[test]
    fn buy_low_sell_high_at_the_ends() {
        assert_eq!(max_profit(&[0, 100]), 100);
    }

    #[test]
    fn the_low_comes_after_the_high() {
        // cannot sell before buying
        assert_eq!(max_profit(&[100, 0]), 0);
    }

    #[test]
    fn best_pair_is_not_the_global_min_and_max() {
        // the lowest price (0) comes after the highest (6)
        assert_eq!(max_profit(&[3, 2, 6, 5, 0, 3]), 4);
    }

    #[test]
    fn largest_allowed_input() {
        // 100 days, the constraint's ceiling: the price slides from 50 down to 0,
        // then climbs to 98. Buy at the bottom, sell on the last day.
        let mut prices: Vec<i32> = (0..50).map(|i| 50 - i).collect();
        prices.extend((0..50).map(|i| i * 2));
        assert_eq!(max_profit(&prices), 98);
    }
}
