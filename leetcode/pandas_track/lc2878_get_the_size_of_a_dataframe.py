"""
2878. Get the Size of a DataFrame · Easy · https://leetcode.com/problems/get-the-size-of-a-dataframe/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem:
Approach:
Time O(?), space O(?)
"""

from typing import List

from _pd import check, frame

# ---------------------------------------------------------------- solution
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    players = frame(['player_id', 'name', 'age', 'position', 'team'],
                    [[846, 'Mason', 21, 'Forward', 'RealMadrid'], [749, 'Riley', 30, 'Winger', 'Barcelona'],
                     [155, 'Bob', 28, 'Striker', 'ManchesterUnited'], [583, 'Isabella', 32, 'Goalkeeper', 'Liverpool'],
                     [388, 'Zachary', 24, 'Midfielder', 'BayernMunich'], [883, 'Ava', 23, 'Defender', 'Chelsea'],
                     [355, 'Violet', 18, 'Striker', 'Juventus'], [247, 'Thomas', 27, 'Striker', 'ParisSaint-Germain'],
                     [761, 'Jack', 33, 'Midfielder', 'ManchesterCity'], [642, 'Charlie', 36, 'Center-back', 'Arsenal']])
    assert list(getDataframeSize(players)) == [10, 5]
