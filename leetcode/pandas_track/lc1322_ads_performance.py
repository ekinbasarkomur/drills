"""
1322. Ads Performance · Easy · https://leetcode.com/problems/ads-performance/
Plan: 30 Days of Pandas · pekiştirme · Statistics

Problem: the click-through rate of each ad, ctr = clicks / (clicks + views) * 100 rounded to 2 decimals; Ignored rows count for nothing, an ad with no clicks or views gets 0; ordered by ctr descending, then ad_id ascending.
Approach: two boolean columns (clicked, viewed), groupby ad_id and sum them, so each True counts as 1; ctr from the two sums, the 0/0 NaN of an ad with only Ignored rows becomes 0 with fillna, then round, reset_index and a two-key sort.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads["clicked"] = ads["action"] == "Clicked"
    ads["viewed"] = ads["action"] == "Viewed"

    counts = ads.groupby(by="ad_id")[["clicked", "viewed"]].sum()
    counts["ctr"] = counts["clicked"] / (counts["clicked"] + counts["viewed"]) * 100
    counts = (
        counts.fillna(0)
        .round(2)[["ctr"]]
        .reset_index()
        .sort_values(by=["ctr", "ad_id"], ascending=[False, True])
    )

    return counts


# ---------------------------------------------------------------- tests

# ctr = clicks / (clicks + views) * 100, rounded to 2 decimals. Ignored rows
# count for nothing, but an ad with only Ignored rows still appears, with 0.
# Ordered by ctr descending, then ad_id ascending on a tie.


def actions(*rows):
    return frame(
        ["ad_id", "user_id", "action"],
        [list(r) for r in rows],
        {"ad_id": "Int64", "user_id": "Int64", "action": "object"},
    )


def test_example_1():
    ads = actions(
        (1, 1, "Clicked"),
        (2, 2, "Clicked"),
        (3, 3, "Viewed"),
        (5, 5, "Ignored"),
        (1, 7, "Ignored"),
        (2, 7, "Viewed"),
        (3, 5, "Clicked"),
        (1, 4, "Viewed"),
        (2, 11, "Viewed"),
        (1, 2, "Clicked"),
    )
    check(
        ads_performance(ads),
        ["ad_id", "ctr"],
        [[1, 66.67], [3, 50.0], [2, 33.33], [5, 0.0]],
        ordered=True,
    )


def test_only_ignored_ad_is_zero_not_missing():
    ads = actions((1, 1, "Clicked"), (2, 1, "Ignored"), (2, 2, "Ignored"))
    check(ads_performance(ads), ["ad_id", "ctr"], [[1, 100.0], [2, 0.0]], ordered=True)


def test_ignored_does_not_dilute_the_rate():
    # ad 1: 1 click, 1 view, 5 ignores -> still 50, not 1/7
    ads = actions(
        (1, 1, "Clicked"),
        (1, 2, "Viewed"),
        (1, 3, "Ignored"),
        (1, 4, "Ignored"),
        (1, 5, "Ignored"),
        (1, 6, "Ignored"),
        (1, 7, "Ignored"),
    )
    check(ads_performance(ads), ["ad_id", "ctr"], [[1, 50.0]])


def test_ties_break_by_ad_id_ascending():
    ads = actions(
        (9, 1, "Clicked"),
        (9, 2, "Viewed"),
        (4, 1, "Clicked"),
        (4, 2, "Viewed"),
        (7, 1, "Clicked"),
        (7, 2, "Viewed"),
    )
    check(
        ads_performance(ads),
        ["ad_id", "ctr"],
        [[4, 50.0], [7, 50.0], [9, 50.0]],
        ordered=True,
    )


def test_rounding():
    # 1 of 3 -> 33.333 -> 33.33 ; 2 of 3 -> 66.666 -> 66.67
    ads = actions(
        (1, 1, "Clicked"),
        (1, 2, "Viewed"),
        (1, 3, "Viewed"),
        (2, 1, "Clicked"),
        (2, 2, "Clicked"),
        (2, 3, "Viewed"),
    )
    check(
        ads_performance(ads), ["ad_id", "ctr"], [[2, 66.67], [1, 33.33]], ordered=True
    )


def test_all_viewed_no_clicks():
    ads = actions((1, 1, "Viewed"), (1, 2, "Viewed"))
    check(ads_performance(ads), ["ad_id", "ctr"], [[1, 0.0]])


def test_empty_table():
    ads = actions()
    check(ads_performance(ads), ["ad_id", "ctr"], [])
