// 2502. Design Memory Allocator · Medium · https://leetcode.com/problems/design-memory-allocator/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Allocator {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Allocator {

    fn new(n: i32) -> Self {
        todo!()
    }
    
    fn allocate(&self, size: i32, m_id: i32) -> i32 {
        todo!()
    }
    
    fn free_memory(&self, m_id: i32) -> i32 {
        todo!()
    }
}

/**
 * Your Allocator object will be instantiated and called as such:
 * let obj = Allocator::new(n);
 * let ret_1: i32 = obj.allocate(size, mID);
 * let ret_2: i32 = obj.free_memory(mID);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Allocator::new(10);
        assert_eq!(obj.allocate(1, 1), 0);
        assert_eq!(obj.allocate(1, 2), 1);
        assert_eq!(obj.allocate(1, 3), 2);
        assert_eq!(obj.free_memory(2), 1);
        assert_eq!(obj.allocate(3, 4), 3);
        assert_eq!(obj.allocate(1, 1), 1);
        assert_eq!(obj.allocate(1, 1), 6);
        assert_eq!(obj.free_memory(1), 3);
        assert_eq!(obj.allocate(10, 2), -1);
        assert_eq!(obj.free_memory(7), 0);
    }
}
