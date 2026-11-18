"""
511. Game Play Analysis I · Easy · https://leetcode.com/problems/game-play-analysis-i/
Plan: 30 Days of Pandas · Gün 20 · Data Aggregation

Problem: the first login date of each player, the earliest event_date in their activity rows, returned as player_id and first_login.
Approach: rename event_date to first_login, groupby player_id and take the min of the date column; the rows are unordered, so the earliest date is the min, not the first row; reset_index turns player_id back into a column.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:

    activity = activity.rename(columns={"event_date": "first_login"}).reset_index()
    return pd.DataFrame(
        activity.groupby("player_id")["first_login"].min()
    ).reset_index()


# ---------------------------------------------------------------- tests

# One row per player with the earliest event_date, renamed `first_login`.
# Rows arrive in no particular order, so "first row per player" is wrong;
# it has to be the minimum date. Any row order.


def logins(*rows):
    return frame(
        ["player_id", "device_id", "event_date", "games_played"],
        [list(r) for r in rows],
        {
            "player_id": "Int64",
            "device_id": "Int64",
            "event_date": "datetime64[ns]",
            "games_played": "Int64",
        },
    )


COLS = ["player_id", "first_login"]


def test_example_1():
    activity = logins(
        (1, 2, "2016-03-01", 5),
        (1, 2, "2016-05-02", 6),
        (2, 3, "2017-06-25", 1),
        (3, 1, "2016-03-02", 0),
        (3, 4, "2018-07-03", 5),
    )
    check(
        game_analysis(activity),
        COLS,
        [[1, "2016-03-01"], [2, "2017-06-25"], [3, "2016-03-02"]],
    )


def test_earliest_date_is_not_the_first_row():
    # player 1's rows arrive newest first; the answer is still the oldest
    activity = logins(
        (1, 2, "2020-12-31", 1),
        (1, 2, "2020-06-15", 1),
        (1, 2, "2020-01-01", 1),
    )
    check(game_analysis(activity), COLS, [[1, "2020-01-01"]])


def test_one_login_per_player():
    activity = logins((5, 1, "2019-01-01", 0), (6, 1, "2019-02-02", 0))
    check(game_analysis(activity), COLS, [[5, "2019-01-01"], [6, "2019-02-02"]])


def test_zero_games_still_counts_as_a_login():
    activity = logins((1, 1, "2019-01-01", 0), (1, 1, "2019-01-02", 9))
    check(game_analysis(activity), COLS, [[1, "2019-01-01"]])


def test_device_does_not_matter():
    activity = logins(
        (1, 9, "2019-03-03", 1), (1, 2, "2019-03-01", 1), (1, 5, "2019-03-02", 1)
    )
    check(game_analysis(activity), COLS, [[1, "2019-03-01"]])


def test_empty_table():
    activity = logins()
    check(game_analysis(activity), COLS, [])
