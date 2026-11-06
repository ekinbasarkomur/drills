"""
2669. Count Artist Occurrences On Spotify Ranking List · Easy · https://leetcode.com/problems/count-artist-occurrences-on-spotify-ranking-list/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_occurrences(spotify: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    spotify = frame(['id', 'track_name', 'artist'], [[303651, "Heart Won't Forget", 'Ed Sheeran'], [1046089, 'Shape of you', 'Sia'], [33445, "I'm the one", 'DJ Khalid'], [811266, 'Young Dumb & Broke', 'DJ Khalid'], [505727, 'Happier', 'Ed Sheeran']], {'id': 'Int64', 'track_name': 'object', 'artist': 'object'})
    check(count_occurrences(spotify), ['artist', 'occurrences'], [['DJ Khalid', 2], ['Ed Sheeran', 2], ['Sia', 1]], ordered=True)
