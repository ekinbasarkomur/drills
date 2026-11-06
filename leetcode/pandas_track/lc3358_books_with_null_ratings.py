"""
3358. Books with NULL Ratings · Easy · https://leetcode.com/problems/books-with-null-ratings/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def find_unrated_books(books: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    books = frame(['book_id', 'title', 'author', 'published_year', 'rating'], [[1, 'The Great Gatsby', 'F. Scott', 1925, 4.5], [2, 'To Kill a Mockingbird', 'Harper Lee', 1960, None], [3, 'Pride and Prejudice', 'Jane Austen', 1813, 4.8], [4, 'The Catcher in the Rye', 'J.D. Salinger', 1951, None], [5, 'Animal Farm', 'George Orwell', 1945, 4.2], [6, 'Lord of the Flies', 'William Golding', 1954, None]], {})
    check(find_unrated_books(books), ['book_id', 'title', 'author', 'published_year'], [[2, 'To Kill a Mockingbird', 'Harper Lee', 1960], [4, 'The Catcher in the Rye', 'J.D. Salinger', 1951], [6, 'Lord of the Flies', 'William Golding', 1954]], ordered=True)
