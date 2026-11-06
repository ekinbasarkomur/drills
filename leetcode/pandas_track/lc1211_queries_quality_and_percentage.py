"""
1211. Queries Quality and Percentage · Easy · https://leetcode.com/problems/queries-quality-and-percentage/
Plan: Paralel hat · SQL

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    queries = frame(['query_name', 'result', 'position', 'rating'], [['Dog', 'Golden Retriever', 1, 5], ['Dog', 'German Shepherd', 2, 5], ['Dog', 'Mule', 200, 1], ['Cat', 'Shirazi', 5, 2], ['Cat', 'Siamese', 3, 3], ['Cat', 'Sphynx', 7, 4]], {'query_name': 'object', 'result': 'object', 'position': 'Int64', 'rating': 'Int64'})
    check(queries_stats(queries), ['query_name', 'quality', 'poor_query_percentage'], [['Dog', 2.5, 33.33], ['Cat', 0.66, 33.33]], ordered=False)
