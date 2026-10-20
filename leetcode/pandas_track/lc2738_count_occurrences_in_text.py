"""
2738. Count Occurrences in Text · Medium · https://leetcode.com/problems/count-occurrences-in-text/
Plan: 30 Days of Pandas · pekiştirme · String Methods

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    # Premium problem: the expected output is not public, so this only runs it.
    files = frame(['file_name', 'content'], [['draft1.txt', 'The stock exchange predicts a bull market which would make many investors happy.'], ['draft2.txt', 'The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market.'], ['final.txt', 'The stock exchange predicts a bull market which would make many investors happy, but analysts warn of possibility of too much optimism and that in fact we are awaiting a bear market. As always predicting the future market is an uncertain game and all investors should follow their instincts and best practices.']], {'file_name': 'object', 'content': 'object'})
    count_occurrences(files)
