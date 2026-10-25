"""
2891. Method Chaining · Easy · https://leetcode.com/problems/method-chaining/
Plan: Paralel hat · Pandas · Introduction to Pandas

Problem: names of the animals heavier than 100 kg, heaviest first, in one chained expression.
Approach: filter with the weight > 100 mask first, then sort_values descending, then pick the name column
Time O(n log n), space O(n)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    return animals[animals["weight"] > 100].sort_values(by=["weight"], ascending=False)[
        ["name"]
    ]


# ---------------------------------------------------------------- tests


def test_example_1():
    animals = frame(
        ["name", "species", "age", "weight"],
        [
            ["Tatiana", "Snake", 98, 464],
            ["Khaled", "Giraffe", 50, 41],
            ["Alex", "Leopard", 6, 328],
            ["Jonathan", "Monkey", 45, 463],
            ["Stefan", "Bear", 100, 50],
            ["Tommy", "Panda", 26, 349],
        ],
        {"name": "object", "species": "object", "age": "Int64", "weight": "Int64"},
    )
    check(
        findHeavyAnimals(animals),
        ["name"],
        [["Tatiana"], ["Jonathan"], ["Tommy"], ["Alex"]],
        ordered=False,
    )
