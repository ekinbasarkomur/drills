// 362. Design Hit Counter · Medium · https://leetcode.com/problems/design-hit-counter/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct HitCounter {

}


impl HitCounter {

    fn new() -> Self {
        todo!()
    }
    
    fn hit(&self, timestamp: i32) {
        todo!()
    }
    
    fn get_hits(&self, timestamp: i32) -> i32 {
        todo!()
    }
}
// ---------------------------------------------------------------- tests

fn main() {}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn example_1() {
        // Premium problem: the expected output is not public, so this only runs it.
        let mut obj = HitCounter::new();
        obj.hit(1);
        obj.hit(2);
        obj.hit(3);
        obj.get_hits(4);
        obj.hit(300);
        obj.get_hits(300);
        obj.get_hits(301);
    }
}
