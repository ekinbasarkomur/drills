"""
1148. Article Views I · Easy · https://leetcode.com/problems/article-views-i/
Plan: 30 Days of Pandas · Gün 4 · Data Filtering

Problem: the authors who viewed at least one of their own articles, as a single column
         named id, sorted ascending.
Approach: keep the rows where author_id equals viewer_id, then reduce them to distinct
          authors. groupby("author_id").count() does that as a side effect: the key moves
          into the index (sorted), no column is left to count, and reset_index turns the
          index back into the only column. k = distinct authors.
Time O(n + k log k), space O(n)
"""

# ---------------------------------------------------------------- solution
import pandas as pd
from _pd import check, frame


def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views["author_id"] == views["viewer_id"]][["author_id"]]
    views = views.groupby("author_id").count()
    views = views.reset_index()
    views = views.rename(columns={"author_id": "id"})
    return views


# ---------------------------------------------------------------- tests


def test_example_1():
    views = frame(
        ["article_id", "author_id", "viewer_id", "view_date"],
        [
            [1, 3, 5, "2019-08-01"],
            [1, 3, 6, "2019-08-02"],
            [2, 7, 7, "2019-08-01"],
            [2, 7, 6, "2019-08-02"],
            [4, 7, 1, "2019-07-22"],
            [3, 4, 4, "2019-07-21"],
            [3, 4, 4, "2019-07-21"],
        ],
        {
            "article_id": "Int64",
            "author_id": "Int64",
            "viewer_id": "Int64",
            "view_date": "datetime64[ns]",
        },
    )
    check(article_views(views), ["id"], [[4], [7]], ordered=False)
