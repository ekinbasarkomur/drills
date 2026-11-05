// 1227. Airplane Seat Assignment Probability · Medium · https://leetcode.com/problems/airplane-seat-assignment-probability/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn nth_person_gets_nth_seat(n: i32) -> f64 {
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
        check!(approx_eq(Solution::nth_person_gets_nth_seat(1), 1.0));
    }

    #[test]
    fn example_2() {
        check!(approx_eq(Solution::nth_person_gets_nth_seat(2), 0.5));
    }
}
