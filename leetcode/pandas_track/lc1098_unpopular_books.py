"""
1098. Unpopular Books · Medium · https://leetcode.com/problems/unpopular-books/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def unpopular_books(books: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    books = frame(['book_id', 'name', 'available_from'], [[1, 'Kalila And Demna', '2010-01-01'], [2, '28 Letters', '2012-05-12'], [3, 'The Hobbit', '2019-06-10'], [4, '13 Reasons Why', '2019-06-01'], [5, 'The Hunger Games', '2008-09-21']], {'book_id': 'Int64', 'name': 'object', 'available_from': 'datetime64[ns]'})
    orders = frame(['order_id', 'book_id', 'quantity', 'dispatch_date'], [[1, 1, 2, '2018-07-26'], [2, 1, 1, '2018-11-05'], [3, 3, 8, '2019-06-11'], [4, 4, 6, '2019-06-05'], [5, 4, 5, '2019-06-20'], [6, 5, 9, '2009-02-02'], [7, 5, 8, '2010-04-13']], {'order_id': 'Int64', 'book_id': 'Int64', 'quantity': 'Int64', 'dispatch_date': 'datetime64[ns]'})
    check(unpopular_books(books, orders), ['book_id', 'name'], [[1, '"Kalila And Demna"'], [2, '"28 Letters"'], [5, '"The Hunger Games"']], ordered=False)
