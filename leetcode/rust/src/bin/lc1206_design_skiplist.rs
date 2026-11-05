// 1206. Design Skiplist · Hard · https://leetcode.com/problems/design-skiplist/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Skiplist {

}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Skiplist {

    fn new() -> Self {
        todo!()
    }
    
    fn search(&self, target: i32) -> bool {
        todo!()
    }
    
    fn add(&self, num: i32) {
        todo!()
    }
    
    fn erase(&self, num: i32) -> bool {
        todo!()
    }
}

/**
 * Your Skiplist object will be instantiated and called as such:
 * let obj = Skiplist::new();
 * let ret_1: bool = obj.search(target);
 * obj.add(num);
 * let ret_3: bool = obj.erase(num);
 */
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        let mut obj = Skiplist::new();
        obj.add(1);
        obj.add(2);
        obj.add(3);
        check_eq!(obj.search(0), false);
        obj.add(4);
        check_eq!(obj.search(1), true);
        check_eq!(obj.erase(0), false);
        check_eq!(obj.erase(1), true);
        check_eq!(obj.search(1), false);
    }
}
