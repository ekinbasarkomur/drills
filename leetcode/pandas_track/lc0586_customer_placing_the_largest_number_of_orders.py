"""
586. Customer Placing the Largest Number of Orders · Easy · https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/
Plan: 30 Days of Pandas · Gün 23 · Data Aggregation

Problem: the customer_number of the customer who placed the most orders; the judge guarantees exactly one such customer.
Approach: groupby customer_number and count the distinct order numbers with nunique, reset_index turns customer_number back into a column; the maximum count is broadcast into a max_orders column and the rows equal to it are kept, so a tie would return every top customer.
Time O(n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:

    customers = pd.DataFrame(
        orders.groupby("customer_number")["order_number"].nunique()
    ).reset_index()
    customers["max_orders"] = customers["order_number"].max()
    return customers[customers["order_number"] == customers["max_orders"]][
        ["customer_number"]
    ]


# ---------------------------------------------------------------- tests

# One column `customer_number`, one row: the customer with the most orders.
# The judge guarantees a single winner, so every test here has one. (The
# follow-up, several customers tied at the top, is not tested.)


def orders_by(*customers):
    # orders_by(1, 2, 3, 3) -> four orders, order_number 1..4, for those customers
    rows = [[i + 1, c] for i, c in enumerate(customers)]
    return frame(
        ["order_number", "customer_number"],
        rows,
        {"order_number": "Int64", "customer_number": "Int64"},
    )


COLS = ["customer_number"]


def test_example_1():
    check(largest_orders(orders_by(1, 2, 3, 3)), COLS, [[3]])


def test_winner_is_not_the_largest_id():
    # customer 1 has 3 orders, customer 9 has 1
    check(largest_orders(orders_by(9, 1, 1, 1)), COLS, [[1]])


def test_winner_is_not_the_first_row():
    check(largest_orders(orders_by(5, 7, 7, 5, 7)), COLS, [[7]])


def test_single_customer():
    check(largest_orders(orders_by(4, 4, 4)), COLS, [[4]])


def test_single_order():
    check(largest_orders(orders_by(2)), COLS, [[2]])


def test_only_one_row_comes_back():
    # three customers, clear winner; the answer must not list the others
    check(largest_orders(orders_by(1, 2, 2, 3, 3, 3)), COLS, [[3]])
