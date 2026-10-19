// 3508. Implement Router · Medium · https://leetcode.com/problems/implement-router/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Router {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Router {

    fn new(memoryLimit: i32) -> Self {
        todo!()
    }
    
    fn add_packet(&self, source: i32, destination: i32, timestamp: i32) -> bool {
        todo!()
    }
    
    fn forward_packet(&self) -> Vec<i32> {
        todo!()
    }
    
    fn get_count(&self, destination: i32, start_time: i32, end_time: i32) -> i32 {
        todo!()
    }
}

/**
 * Your Router object will be instantiated and called as such:
 * let obj = Router::new(memoryLimit);
 * let ret_1: bool = obj.add_packet(source, destination, timestamp);
 * let ret_2: Vec<i32> = obj.forward_packet();
 * let ret_3: i32 = obj.get_count(destination, startTime, endTime);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Router::new(3);
        assert_eq!(obj.add_packet(1, 4, 90), true);
        assert_eq!(obj.add_packet(2, 5, 90), true);
        assert_eq!(obj.add_packet(1, 4, 90), false);
        assert_eq!(obj.add_packet(3, 5, 95), true);
        assert_eq!(obj.add_packet(4, 5, 105), true);
        let want: Vec<i32> = vec![2, 5, 90];
        assert_eq!(obj.forward_packet(), want);
        assert_eq!(obj.add_packet(5, 2, 110), true);
        assert_eq!(obj.get_count(5, 100, 110), 1);
    }

    #[test]
    fn example_2() {
        let mut obj = Router::new(2);
        assert_eq!(obj.add_packet(7, 4, 90), true);
        let want: Vec<i32> = vec![7, 4, 90];
        assert_eq!(obj.forward_packet(), want);
        let want: Vec<i32> = vec![];
        assert_eq!(obj.forward_packet(), want);
    }
}
