// 295. Find Median from Data Stream · Hard · https://leetcode.com/problems/find-median-from-data-stream/
// Plan: Aşama 2 · Data Stream ve Heap
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MedianFinder {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {

    fn new() -> Self {
        todo!()
    }
    
    fn add_num(&self, num: i32) {
        todo!()
    }
    
    fn find_median(&self) -> f64 {
        todo!()
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MedianFinder::new();
        obj.add_num(1);
        obj.add_num(2);
        check!(approx_eq(obj.find_median(), 1.5));
        obj.add_num(3);
        check!(approx_eq(obj.find_median(), 2.0));
    }
}
