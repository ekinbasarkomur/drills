// 528. Random Pick with Weight · Medium · https://leetcode.com/problems/random-pick-with-weight/
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

    fn new(w: Vec<i32>) -> Self {
        todo!()
    }
    
    fn pick_index(&self) -> i32 {
        todo!()
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(w);
 * let ret_1: i32 = obj.pick_index();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Solution::new(vec![1]);
        obj.pick_index();
    }

    #[test]
    fn example_2() {
        let mut obj = Solution::new(vec![1, 3]);
        obj.pick_index();
        obj.pick_index();
        obj.pick_index();
        obj.pick_index();
        obj.pick_index();
    }
}
