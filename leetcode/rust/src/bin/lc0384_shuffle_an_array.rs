// 384. Shuffle an Array · Medium · https://leetcode.com/problems/shuffle-an-array/
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

    fn new(nums: Vec<i32>) -> Self {
        todo!()
    }
    
    fn reset(&self) -> Vec<i32> {
        todo!()
    }
    
    fn shuffle(&self) -> Vec<i32> {
        todo!()
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * let obj = Solution::new(nums);
 * let ret_1: Vec<i32> = obj.reset();
 * let ret_2: Vec<i32> = obj.shuffle();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Solution::new(vec![1, 2, 3]);
        obj.shuffle();
        let want: Vec<i32> = vec![1, 2, 3];
        assert_eq!(obj.reset(), want);
        obj.shuffle();
    }
}
