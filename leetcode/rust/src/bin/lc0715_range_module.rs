// 715. Range Module · Hard · https://leetcode.com/problems/range-module/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct RangeModule {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RangeModule {

    fn new() -> Self {
        todo!()
    }
    
    fn add_range(&self, left: i32, right: i32) {
        todo!()
    }
    
    fn query_range(&self, left: i32, right: i32) -> bool {
        todo!()
    }
    
    fn remove_range(&self, left: i32, right: i32) {
        todo!()
    }
}

/**
 * Your RangeModule object will be instantiated and called as such:
 * let obj = RangeModule::new();
 * obj.add_range(left, right);
 * let ret_2: bool = obj.query_range(left, right);
 * obj.remove_range(left, right);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = RangeModule::new();
        obj.add_range(10, 20);
        obj.remove_range(14, 16);
        check_eq!(obj.query_range(10, 14), true);
        check_eq!(obj.query_range(13, 15), false);
        check_eq!(obj.query_range(16, 17), true);
    }
}
