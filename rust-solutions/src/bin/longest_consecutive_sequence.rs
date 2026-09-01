// 128. Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/
//
// Problem: length of the longest run of consecutive integers that can be formed
//          from nums. Order in the array does not matter.
// Approach:
// Time O(?), space O(?)   -- the problem demands O(n)

struct Solution;

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let _ = nums;
        todo!()
    }
}

fn main() {
    println!("{}", Solution::longest_consecutive(vec![2, 20, 4, 10, 3, 4, 5]));
    println!("{}", Solution::longest_consecutive(vec![0, 3, 2, 5, 4, 6, 1, 1]));
}

#[cfg(test)]
mod tests {
    use super::*;

    fn longest(nums: &[i32]) -> i32 {
        Solution::longest_consecutive(nums.to_vec())
    }

    #[test]
    fn example_1() {
        assert_eq!(longest(&[2, 20, 4, 10, 3, 4, 5]), 4);
    }

    #[test]
    fn example_2() {
        assert_eq!(longest(&[0, 3, 2, 5, 4, 6, 1, 1]), 7);
    }

    #[test]
    fn empty_array() {
        assert_eq!(longest(&[]), 0);
    }

    #[test]
    fn single_element() {
        assert_eq!(longest(&[7]), 1);
    }

    #[test]
    fn all_duplicates_of_one_value() {
        assert_eq!(longest(&[5, 5, 5, 5]), 1);
    }

    #[test]
    fn no_two_numbers_are_consecutive() {
        assert_eq!(longest(&[10, 30, 50, 70]), 1);
    }

    #[test]
    fn already_sorted() {
        assert_eq!(longest(&[1, 2, 3, 4, 5]), 5);
    }

    #[test]
    fn given_in_descending_order() {
        assert_eq!(longest(&[5, 4, 3, 2, 1]), 5);
    }

    #[test]
    fn two_runs_and_the_longer_one_comes_second() {
        assert_eq!(longest(&[1, 2, 3, 100, 101, 102, 103]), 4);
    }

    #[test]
    fn negative_numbers() {
        assert_eq!(longest(&[-3, -2, -1, 0, 1]), 5);
    }

    #[test]
    fn run_straddling_zero_with_a_gap() {
        assert_eq!(longest(&[-5, -4, 100, -3, 7, -1, 0]), 3);
    }

    #[test]
    fn value_range_extremes() {
        // watch out for overflow: num + 1 on i32::MAX would wrap
        assert_eq!(longest(&[1_000_000_000, 999_999_999, -1_000_000_000]), 2);
    }

    #[test]
    fn duplicates_inside_a_run_do_not_inflate_it() {
        assert_eq!(longest(&[1, 2, 2, 3, 3, 3, 4]), 4);
    }

    #[test]
    fn large_input_stays_linear() {
        // 100_000 elements in one unbroken run, handed over shuffled.
        // An O(n^2) solution will hang here rather than fail.
        let n = 100_000i32;
        let mut nums: Vec<i32> = (0..n).collect();

        // deterministic shuffle, no rand crate
        let mut state = 0x2545_F491_4F6C_DD1Du64;
        for i in (1..nums.len()).rev() {
            state ^= state << 13;
            state ^= state >> 7;
            state ^= state << 17;
            let j = (state % (i as u64 + 1)) as usize;
            nums.swap(i, j);
        }

        assert_eq!(longest(&nums), n);
    }
}
