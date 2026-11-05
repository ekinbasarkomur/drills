// 478. Generate Random Point in a Circle · Medium · https://leetcode.com/problems/generate-random-point-in-a-circle/
// Plan: Aşama 5 · Olasılık ve Matematik
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Solution {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Solution {

    fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        todo!()
    }
    
    fn rand_point(&self) -> Vec<f64> {
        todo!()
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(radius, x_center, y_center);
 * let ret_1: Vec<f64> = obj.rand_point();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Solution::new(1.0, 0.0, 0.0);
        check!(approx_eq_vec(&obj.rand_point(), &vec![-0.02493, -0.38077]));
        check!(approx_eq_vec(&obj.rand_point(), &vec![0.82314, 0.38945]));
        check!(approx_eq_vec(&obj.rand_point(), &vec![0.36572, 0.17248]));
    }
}
