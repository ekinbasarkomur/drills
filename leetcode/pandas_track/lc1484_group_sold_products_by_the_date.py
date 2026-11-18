"""
1484. Group Sold Products By The Date · Easy · https://leetcode.com/problems/group-sold-products-by-the-date/
Plan: 30 Days of Pandas · Gün 24 · Data Aggregation

Problem: for each sell_date, the number of different products sold and their names sorted lexicographically and joined with commas; ordered by sell_date.
Approach: drop duplicate rows and sort by product first, append a comma to every product, then groupby sell_date and aggregate twice: nunique for the count and sum, which concatenates the strings in sorted order; the trailing comma is cut with str[:-1].
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities = activities.drop_duplicates().sort_values("product")
    activities["product"] = activities["product"] + ","
    group = activities.groupby("sell_date")
    sold = pd.DataFrame(
        group["product"].agg(num_sold="nunique", products="sum")
    ).reset_index()
    sold["products"] = sold["products"].str[:-1]
    print(sold)
    return sold


# ---------------------------------------------------------------- tests

# One row per date: how many DIFFERENT products were sold, and their names
# joined with "," in sorted order, no spaces. Duplicate rows (same product,
# same day) count once. Rows ordered by sell_date.
# (LeetCode's example prints "T-shirt" in the output for a "T-Shirt" input;
# that is a typo on their page, the real judge keeps the input spelling.)


def sales(*rows):
    return frame(
        ["sell_date", "product"],
        [list(r) for r in rows],
        {"sell_date": "datetime64[ns]", "product": "object"},
    )


COLS = ["sell_date", "num_sold", "products"]


def test_example_1():
    activities = sales(
        ("2020-05-30", "Headphone"),
        ("2020-06-01", "Pencil"),
        ("2020-06-02", "Mask"),
        ("2020-05-30", "Basketball"),
        ("2020-06-01", "Bible"),
        ("2020-06-02", "Mask"),
        ("2020-05-30", "T-Shirt"),
    )
    check(
        categorize_products(activities),
        COLS,
        [
            ["2020-05-30", 3, "Basketball,Headphone,T-Shirt"],
            ["2020-06-01", 2, "Bible,Pencil"],
            ["2020-06-02", 1, "Mask"],
        ],
        ordered=True,
    )


def test_duplicates_count_once():
    activities = sales(
        ("2020-01-01", "Mask"),
        ("2020-01-01", "Mask"),
        ("2020-01-01", "Mask"),
    )
    check(categorize_products(activities), COLS, [["2020-01-01", 1, "Mask"]])


def test_names_are_sorted_not_in_arrival_order():
    activities = sales(
        ("2020-01-01", "Zebra"),
        ("2020-01-01", "Apple"),
        ("2020-01-01", "Mango"),
    )
    check(
        categorize_products(activities),
        COLS,
        [["2020-01-01", 3, "Apple,Mango,Zebra"]],
    )


def test_dates_are_ordered():
    activities = sales(
        ("2020-03-03", "C"),
        ("2020-01-01", "A"),
        ("2020-02-02", "B"),
    )
    check(
        categorize_products(activities),
        COLS,
        [["2020-01-01", 1, "A"], ["2020-02-02", 1, "B"], ["2020-03-03", 1, "C"]],
        ordered=True,
    )


def test_same_product_on_different_days():
    activities = sales(
        ("2020-01-01", "Mask"),
        ("2020-01-02", "Mask"),
        ("2020-01-02", "Glove"),
    )
    check(
        categorize_products(activities),
        COLS,
        [["2020-01-01", 1, "Mask"], ["2020-01-02", 2, "Glove,Mask"]],
        ordered=True,
    )


def test_no_spaces_after_commas():
    activities = sales(("2020-01-01", "B"), ("2020-01-01", "A"))
    check(categorize_products(activities), COLS, [["2020-01-01", 2, "A,B"]])
