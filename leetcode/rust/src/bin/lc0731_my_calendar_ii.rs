// 731. My Calendar II · Medium · https://leetcode.com/problems/my-calendar-ii/
// Plan: Aşama 2 · Intervals ve Sweep Line
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct MyCalendarTwo {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyCalendarTwo {

    fn new() -> Self {
        todo!()
    }
    
    fn book(&self, start_time: i32, end_time: i32) -> bool {
        todo!()
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * let obj = MyCalendarTwo::new();
 * let ret_1: bool = obj.book(startTime, endTime);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = MyCalendarTwo::new();
        check_eq!(obj.book(10, 20), true);
        check_eq!(obj.book(50, 60), true);
        check_eq!(obj.book(10, 40), true);
        check_eq!(obj.book(5, 15), false);
        check_eq!(obj.book(5, 10), true);
        check_eq!(obj.book(25, 55), true);
    }
}
