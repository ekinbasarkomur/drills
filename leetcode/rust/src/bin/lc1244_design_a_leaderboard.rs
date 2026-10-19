// 1244. Design A Leaderboard · Medium · https://leetcode.com/problems/design-a-leaderboard/
// Plan: Aşama 3 · Order Book ve Sistem Tasarımı
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

// ---------------------------------------------------------------- solution
struct Leaderboard {

}


impl Leaderboard {

    fn new() -> Self {
        todo!()
    }
    
    fn add_score(&self, player_id: i32, score: i32) {
        todo!()
    }
    
    fn top(&self, k: i32) -> i32 {
        todo!()
    }
    
    fn reset(&self, player_id: i32) {
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
        let mut obj = Leaderboard::new();
        obj.add_score(1, 73);
        obj.add_score(2, 56);
        obj.add_score(3, 39);
        obj.add_score(4, 51);
        obj.add_score(5, 4);
        obj.top(1);
        obj.reset(1);
        obj.reset(2);
        obj.add_score(2, 51);
        obj.top(3);
    }
}
