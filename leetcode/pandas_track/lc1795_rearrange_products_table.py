"""
1795. Rearrange Products Table · Easy · https://leetcode.com/problems/rearrange-products-table/
Plan: 30 Days of Pandas · Gün 15 · Data Manipulation

Problem: turn the wide products table (one column per store) into long rows of product_id, store, price, leaving out stores where the product is not sold (null).
Approach: melt with product_id as the id column so each store column becomes a store/price row, drop the null prices and sort by product_id.
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:

    products = products.melt(
        id_vars="product_id",
        var_name="store",
        value_name="price",
    )
    return products.dropna(subset=["price"]).sort_values(by="product_id")


# ---------------------------------------------------------------- tests


def test_example_1():
    products = frame(
        ["product_id", "store1", "store2", "store3"],
        [[0, 95, 100, 105], [1, 70, None, 80]],
        {
            "product_id": "Int64",
            "store1": "Int64",
            "store2": "Int64",
            "store3": "Int64",
        },
    )
    check(
        rearrange_products_table(products),
        ["product_id", "store", "price"],
        [
            [0, "store1", 95],
            [0, "store2", 100],
            [0, "store3", 105],
            [1, "store1", 70],
            [1, "store3", 80],
        ],
        ordered=False,
    )
