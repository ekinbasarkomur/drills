// 729. My Calendar I · Medium · https://leetcode.com/problems/my-calendar-i/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyCalendar {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendar {

    fn new() -> Self {
        todo!()
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> bool {
        todo!()
    }
}

/**
 * Your MyCalendar object will be instantiated and called as such:
 * let obj = MyCalendar::new();
 * let ret_1: bool = obj.book(startTime, endTime);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyCalendar::new();
        check_eq!(obj.book(10, 20), true);
        check_eq!(obj.book(15, 25), false);
        check_eq!(obj.book(20, 30), true);
    }
}
