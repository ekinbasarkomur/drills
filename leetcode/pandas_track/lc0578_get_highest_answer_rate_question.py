"""
578. Get Highest Answer Rate Question · Medium · https://leetcode.com/problems/get-highest-answer-rate-question/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def get_the_question(survey_log: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    survey_log = frame(['id', 'action', 'question_id', 'answer_id', 'q_num', 'timestamp'], [[5, 'show', 285, None, 1, 123], [5, 'answer', 285, 124124, 1, 124], [5, 'show', 369, None, 2, 125], [5, 'skip', 369, None, 2, 126]], {'id': 'Int64', 'action': 'object', 'question_id': 'Int64', 'answer_id': 'Int64', 'q_num': 'Int64', 'timestamp': 'Int64'})
    check(get_the_question(survey_log), ['survey_log'], [[285]], ordered=False)
