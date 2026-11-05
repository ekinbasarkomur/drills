// 1146. Snapshot Array · Medium · https://leetcode.com/problems/snapshot-array/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct SnapshotArray {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SnapshotArray {

    fn new(length: i32) -> Self {
        todo!()
    }
    
    fn set(&self, index: i32, val: i32) {
        todo!()
    }
    
    fn snap(&self) -> i32 {
        todo!()
    }
    
    fn get(&self, index: i32, snap_id: i32) -> i32 {
        todo!()
    }
}

/**
 * Your SnapshotArray object will be instantiated and called as such:
 * let obj = SnapshotArray::new(length);
 * obj.set(index, val);
 * let ret_2: i32 = obj.snap();
 * let ret_3: i32 = obj.get(index, snap_id);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = SnapshotArray::new(3);
        obj.set(0, 5);
        check_eq!(obj.snap(), 0);
        obj.set(0, 6);
        check_eq!(obj.get(0, 0), 5);
    }
}
