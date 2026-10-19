// 2286. Booking Concert Tickets in Groups · Hard · https://leetcode.com/problems/booking-concert-tickets-in-groups/
// Plan: Aşama 5 · Segment Tree ve Fenwick
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct BookMyShow {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl BookMyShow {

    fn new(n: i32, m: i32) -> Self {
        todo!()
    }
    
    fn gather(&self, k: i32, max_row: i32) -> Vec<i32> {
        todo!()
    }
    
    fn scatter(&self, k: i32, max_row: i32) -> bool {
        todo!()
    }
}

/**
 * Your BookMyShow object will be instantiated and called as such:
 * let obj = BookMyShow::new(n, m);
 * let ret_1: Vec<i32> = obj.gather(k, maxRow);
 * let ret_2: bool = obj.scatter(k, maxRow);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = BookMyShow::new(2, 5);
        let want: Vec<i32> = vec![0, 0];
        assert_eq!(obj.gather(4, 0), want);
        let want: Vec<i32> = vec![];
        assert_eq!(obj.gather(2, 0), want);
        assert_eq!(obj.scatter(5, 1), true);
        assert_eq!(obj.scatter(5, 1), false);
    }
}
