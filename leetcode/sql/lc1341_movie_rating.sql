-- 1341. Movie Rating · Medium · https://leetcode.com/problems/movie-rating/
-- Plan: Paralel hat · SQL
--
-- Problem:
-- Approach:
-- Time O(?), space O(?)

-- ---------------------------------------------------------------- solution
# Write your MySQL query statement below
-- TODO: solve, then delete this line
-- ---------------------------------------------------------------- tests
-- schema: Create table If Not Exists Movies (movie_id int, title varchar(30))
-- schema: Create table If Not Exists Users (user_id int, name varchar(30))
-- schema: Create table If Not Exists MovieRating (movie_id int, user_id int, rating int, created_at date)
-- case: {"headers": {"Movies": ["movie_id", "title"], "Users": ["user_id", "name"], "MovieRating": ["movie_id", "user_id", "rating", "created_at"]}, "rows": {"Movies": [[1, "Avengers"], [2, "Frozen 2"], [3, "Joker"]], "Users": [[1, "Daniel"], [2, "Monica"], [3, "Maria"], [4, "James"]], "MovieRating": [[1, 1, 3, "2020-01-12"], [1, 2, 4, "2020-02-11"], [1, 3, 2, "2020-02-12"], [1, 4, 1, "2020-01-01"], [2, 1, 5, "2020-02-17"], [2, 2, 2, "2020-02-01"], [2, 3, 2, "2020-03-01"], [3, 1, 3, "2020-02-22"], [3, 2, 4, "2020-02-25"]]}}
-- expect: {"columns": ["results"], "rows": [["Daniel"], ["Frozen 2"]], "ordered": false}
