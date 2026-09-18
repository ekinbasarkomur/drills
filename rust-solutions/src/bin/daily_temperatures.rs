// 739. Daily Temperatures
// https://leetcode.com/problems/daily-temperatures/
//
// Problem: result[i] is how many days you wait after day i for a warmer
//          temperature, or 0 if none ever comes.
// Note: Days waiting for a warmer day pile up in the order they arrived, and
//       the newest one is always resolved first -- a stack of pending indices.
// Approach:
// Time O(?), space O(?)

struct Solution;

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let _ = (temperatures,);
        todo!()
    }
}

fn main() {
    println!("{:?}", Solution::daily_temperatures(vec![30, 38, 30, 36, 35, 40, 28]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn daily_temperatures(temperatures: &[i32]) -> Vec<i32> {
        Solution::daily_temperatures(temperatures.to_vec())
    }

    #[test]
    fn example_1() {
        assert_eq!(daily_temperatures(&[30, 38, 30, 36, 35, 40, 28]), vec![1, 4, 1, 2, 1, 0, 0]);
    }

    #[test]
    fn example_2() {
        // it only ever gets colder
        assert_eq!(daily_temperatures(&[22, 21, 20]), vec![0, 0, 0]);
    }

    #[test]
    fn single_day() {
        assert_eq!(daily_temperatures(&[50]), vec![0]);
    }

    #[test]
    fn two_days_warming() {
        assert_eq!(daily_temperatures(&[1, 2]), vec![1, 0]);
    }

    #[test]
    fn two_days_cooling() {
        assert_eq!(daily_temperatures(&[2, 1]), vec![0, 0]);
    }

    #[test]
    fn flat_week() {
        // equal is not warmer
        assert_eq!(daily_temperatures(&[5, 5, 5]), vec![0, 0, 0]);
    }

    #[test]
    fn the_classic_leetcode_case() {
        assert_eq!(daily_temperatures(&[73, 74, 75, 71, 69, 72, 76, 73]), vec![1, 1, 4, 2, 1, 1, 0, 0]);
    }

    #[test]
    fn one_warm_day_resolves_everything() {
        assert_eq!(daily_temperatures(&[1, 1, 1, 100]), vec![3, 2, 1, 0]);
    }

    #[test]
    fn the_warmest_day_is_first() {
        assert_eq!(daily_temperatures(&[100, 1, 1, 1]), vec![0, 0, 0, 0]);
    }

    #[test]
    fn strictly_ascending() {
        assert_eq!(daily_temperatures(&[1, 2, 3, 4, 5]), vec![1, 1, 1, 1, 0]);
    }

    #[test]
    fn strictly_descending() {
        assert_eq!(daily_temperatures(&[5, 4, 3, 2, 1]), vec![0, 0, 0, 0, 0]);
    }

    #[test]
    fn largest_allowed_input() {
        // 100_000 days all at 50 except the last at 100: every earlier day waits
        // for that final one. An O(n^2) solution will hang here rather than fail.
        let mut temperatures = vec![50; 100_000];
        temperatures[99_999] = 100;
        let expected: Vec<i32> = (0..100_000).map(|i| 99_999 - i).collect();
        assert_eq!(daily_temperatures(&temperatures), expected);
    }
}
