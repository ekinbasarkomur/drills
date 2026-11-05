// 289. Game of Life · Medium · https://leetcode.com/problems/game-of-life/
// Plan: Aşama 5 · Simülasyon ve Ayrıştırma
//
// Problem:
// Approach:
// Time O(?), space O(?)

#[allow(unused_imports)]
use leetcode::*;

struct Solution;

// ---------------------------------------------------------------- solution
impl Solution {
    pub fn game_of_life(board: &mut Vec<Vec<i32>>) {
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
        let mut board: Vec<Vec<i32>> = vec![vec![0, 1, 0], vec![0, 0, 1], vec![1, 1, 1], vec![0, 0, 0]];
        Solution::game_of_life(&mut board);
        let want: Vec<Vec<i32>> = vec![vec![0, 0, 0], vec![1, 0, 1], vec![0, 1, 1], vec![0, 1, 0]];
        check_eq!(board, want);
    }

    #[test]
    fn example_2() {
        let mut board: Vec<Vec<i32>> = vec![vec![1, 1], vec![1, 0]];
        Solution::game_of_life(&mut board);
        let want: Vec<Vec<i32>> = vec![vec![1, 1], vec![1, 1]];
        check_eq!(board, want);
    }
}
