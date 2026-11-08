"""
1173. Immediate Food Delivery I · Easy · https://leetcode.com/problems/immediate-food-delivery-i/
Plan: 30 Days of Pandas · Gün 17 · Statistics

Problem: the share of orders whose order date equals the customer's preferred delivery date, as a percentage rounded to 2 decimals.
Approach: mask order_date == customer_pref_delivery_date; the masked frame's size over the whole frame's size is the immediate share (both count cells over the same columns, so the ratio equals the row ratio); times 100, round to 2, wrap in a one-row DataFrame.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:

    perc = round(
        (
            delivery[
                delivery["order_date"] == delivery["customer_pref_delivery_date"]
            ].size
            / delivery.size
        )
        * 100,
        2,
    )
    print(perc)
    return pd.DataFrame({"immediate_percentage": [perc]})


# ---------------------------------------------------------------- tests

# An order is immediate when order_date == customer_pref_delivery_date. The
# answer is one row, one column `immediate_percentage`: immediate orders over
# all orders, times 100, rounded to 2 decimals.


def deliveries(*rows):
    return frame(
        ["delivery_id", "customer_id", "order_date", "customer_pref_delivery_date"],
        [list(r) for r in rows],
        {
            "delivery_id": "Int64",
            "customer_id": "Int64",
            "order_date": "datetime64[ns]",
            "customer_pref_delivery_date": "datetime64[ns]",
        },
    )


def test_example_1():
    delivery = deliveries(
        (1, 1, "2019-08-01", "2019-08-02"),
        (2, 5, "2019-08-02", "2019-08-02"),
        (3, 1, "2019-08-11", "2019-08-11"),
        (4, 3, "2019-08-24", "2019-08-26"),
        (5, 4, "2019-08-21", "2019-08-22"),
        (6, 2, "2019-08-11", "2019-08-13"),
    )
    check(food_delivery(delivery), ["immediate_percentage"], [[33.33]])


def test_all_immediate():
    delivery = deliveries(
        (1, 1, "2019-08-01", "2019-08-01"),
        (2, 2, "2019-08-02", "2019-08-02"),
    )
    check(food_delivery(delivery), ["immediate_percentage"], [[100.0]])


def test_none_immediate():
    delivery = deliveries(
        (1, 1, "2019-08-01", "2019-08-02"),
        (2, 2, "2019-08-02", "2019-08-05"),
    )
    check(food_delivery(delivery), ["immediate_percentage"], [[0.0]])


def test_rounds_to_two_decimals():
    # 2 of 3 -> 66.666... -> 66.67
    delivery = deliveries(
        (1, 1, "2019-08-01", "2019-08-01"),
        (2, 2, "2019-08-02", "2019-08-02"),
        (3, 3, "2019-08-03", "2019-08-09"),
    )
    check(food_delivery(delivery), ["immediate_percentage"], [[66.67]])


def test_same_customer_counts_per_order_not_per_customer():
    # customer 1 has one immediate and one scheduled order: 1 of 2 -> 50
    delivery = deliveries(
        (1, 1, "2019-08-01", "2019-08-01"),
        (2, 1, "2019-08-02", "2019-08-03"),
    )
    check(food_delivery(delivery), ["immediate_percentage"], [[50.0]])


def test_single_immediate_order():
    delivery = deliveries((1, 1, "2019-08-01", "2019-08-01"))
    check(food_delivery(delivery), ["immediate_percentage"], [[100.0]])
