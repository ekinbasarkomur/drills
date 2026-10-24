"""
2878. Get the Size of a DataFrame · Easy · https://leetcode.com/problems/get-the-size-of-a-dataframe/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: return [number of rows, number of columns] of the players DataFrame.
Approach: df.shape is the (rows, columns) tuple; turn it into a list.
Time O(1), space O(1)
"""

from typing import List

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    print(players.shape)

    return [players.shape[0], players.shape[1]]


# ---------------------------------------------------------------- tests


def test_example_1():
    players = frame(
        ["player_id", "name", "age", "position", "team"],
        [
            [846, "Mason", 21, "Forward", "RealMadrid"],
            [749, "Riley", 30, "Winger", "Barcelona"],
            [155, "Bob", 28, "Striker", "ManchesterUnited"],
            [583, "Isabella", 32, "Goalkeeper", "Liverpool"],
            [388, "Zachary", 24, "Midfielder", "BayernMunich"],
            [883, "Ava", 23, "Defender", "Chelsea"],
            [355, "Violet", 18, "Striker", "Juventus"],
            [247, "Thomas", 27, "Striker", "ParisSaint-Germain"],
            [761, "Jack", 33, "Midfielder", "ManchesterCity"],
            [642, "Charlie", 36, "Center-back", "Arsenal"],
        ],
    )
    assert list(getDataframeSize(players)) == [10, 5]
