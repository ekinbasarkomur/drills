"""
1364. Number of Trusted Contacts of a Customer · Medium · https://leetcode.com/problems/number-of-trusted-contacts-of-a-customer/
Plan: Paralel hat · Pandas · LeetCode Database

Problem:
Approach:
Time O(?), space O(?)
"""

from _pd import check, frame  # isort: skip

# ---------------------------------------------------------------- solution
import pandas as pd

def count_trusted_contacts(customers: pd.DataFrame, contacts: pd.DataFrame, invoices: pd.DataFrame) -> pd.DataFrame:
    raise NotImplementedError


# ---------------------------------------------------------------- tests

def test_example_1():
    customers = frame(['customer_id', 'customer_name', 'email'], [[1, 'Alice', 'alice@leetcode.com'], [2, 'Bob', 'bob@leetcode.com'], [13, 'John', 'john@leetcode.com'], [6, 'Alex', 'alex@leetcode.com']], {'customer_id': 'Int64', 'customer_name': 'object', 'email': 'object'})
    contacts = frame(['user_id', 'contact_name', 'contact_email'], [[1, 'Bob', 'bob@leetcode.com'], [1, 'John', 'john@leetcode.com'], [1, 'Jal', 'jal@leetcode.com'], [2, 'Omar', 'omar@leetcode.com'], [2, 'Meir', 'meir@leetcode.com'], [6, 'Alice', 'alice@leetcode.com']], {'user_id': 'Int64', 'contact_name': 'object', 'contact_email': 'object'})
    invoices = frame(['invoice_id', 'price', 'user_id'], [[77, 100, 1], [88, 200, 1], [99, 300, 2], [66, 400, 2], [55, 500, 13], [44, 60, 6]], {'invoice_id': 'Int64', 'price': 'Int64', 'user_id': 'Int64'})
    check(count_trusted_contacts(customers, contacts, invoices), ['invoice_id', 'customer_name', 'price', 'contacts_cnt', 'trusted_contacts_cnt'], [[44, 'Alex', 60, 1, 1], [55, 'John', 500, 0, 0], [66, 'Bob', 400, 2, 0], [77, 'Alice', 100, 3, 2], [88, 'Alice', 200, 3, 2], [99, 'Bob', 300, 2, 0]], ordered=True)
