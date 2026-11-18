"""
1693. Daily Leads and Partners · Easy · https://leetcode.com/problems/daily-leads-and-partners/
Plan: 30 Days of Pandas · Gün 25 · Data Aggregation

Problem: for each date_id and make_name, the number of distinct lead_id and distinct partner_id values, as unique_leads and unique_partners.
Approach: groupby on the two keys (date_id, make_name) and named agg with nunique on lead_id and on partner_id, so repeated ids count once; reset_index turns the two-level MultiIndex back into columns.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (
        daily_sales.groupby(["date_id", "make_name"])
        .agg(
            unique_leads=("lead_id", "nunique"),
            unique_partners=("partner_id", "nunique"),
        )
        .reset_index()
    )


# ---------------------------------------------------------------- tests

# Group by TWO keys, date_id and make_name; for each group count DISTINCT
# lead_ids and DISTINCT partner_ids, two different columns. Duplicate rows
# count once. Any row order.


def sales(*rows):
    return frame(
        ["date_id", "make_name", "lead_id", "partner_id"],
        [list(r) for r in rows],
        {
            "date_id": "datetime64[ns]",
            "make_name": "object",
            "lead_id": "Int64",
            "partner_id": "Int64",
        },
    )


COLS = ["date_id", "make_name", "unique_leads", "unique_partners"]


def test_example_1():
    daily_sales = sales(
        ("2020-12-08", "toyota", 0, 1),
        ("2020-12-08", "toyota", 1, 0),
        ("2020-12-08", "toyota", 1, 2),
        ("2020-12-07", "toyota", 0, 2),
        ("2020-12-07", "toyota", 0, 1),
        ("2020-12-08", "honda", 1, 2),
        ("2020-12-08", "honda", 2, 1),
        ("2020-12-07", "honda", 0, 1),
        ("2020-12-07", "honda", 1, 2),
        ("2020-12-07", "honda", 2, 1),
    )
    check(
        daily_leads_and_partners(daily_sales),
        COLS,
        [
            ["2020-12-08", "toyota", 2, 3],
            ["2020-12-07", "toyota", 1, 2],
            ["2020-12-08", "honda", 2, 2],
            ["2020-12-07", "honda", 3, 2],
        ],
    )


def test_exact_duplicate_rows_count_once():
    daily_sales = sales(
        ("2020-01-01", "ford", 5, 9),
        ("2020-01-01", "ford", 5, 9),
        ("2020-01-01", "ford", 5, 9),
    )
    check(daily_leads_and_partners(daily_sales), COLS, [["2020-01-01", "ford", 1, 1]])


def test_leads_and_partners_are_counted_separately():
    # one lead, many partners
    daily_sales = sales(
        ("2020-01-01", "ford", 1, 1),
        ("2020-01-01", "ford", 1, 2),
        ("2020-01-01", "ford", 1, 3),
        ("2020-01-01", "ford", 1, 4),
    )
    check(daily_leads_and_partners(daily_sales), COLS, [["2020-01-01", "ford", 1, 4]])


def test_same_make_different_days_are_different_groups():
    daily_sales = sales(
        ("2020-01-01", "ford", 1, 1),
        ("2020-01-02", "ford", 2, 2),
        ("2020-01-02", "ford", 3, 2),
    )
    check(
        daily_leads_and_partners(daily_sales),
        COLS,
        [["2020-01-01", "ford", 1, 1], ["2020-01-02", "ford", 2, 1]],
    )


def test_same_day_different_makes_are_different_groups():
    daily_sales = sales(
        ("2020-01-01", "ford", 1, 1),
        ("2020-01-01", "kia", 1, 1),
        ("2020-01-01", "kia", 2, 1),
    )
    check(
        daily_leads_and_partners(daily_sales),
        COLS,
        [["2020-01-01", "ford", 1, 1], ["2020-01-01", "kia", 2, 1]],
    )


def test_empty_table():
    check(daily_leads_and_partners(sales()), COLS, [])
