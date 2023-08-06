# 183. Customers Who Never Order
# Table: Customers
# +-------------+---------+
# | Column Name | Type    |
# +-------------+---------+
# | id          | int     |
# | name        | varchar |
# +-------------+---------+
# id is the primary key (column with unique values) for this table.
# Each row of this table indicates the ID and name of a customer.
# Table: Orders
# +-------------+------+
# | Column Name | Type |
# +-------------+------+
# | id          | int  |
# | customerId  | int  |
# +-------------+------+
# id is the primary key (column with unique values) for this table.
# customerId is a foreign key (reference columns) of the ID from the Customers table.
# Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
# Write a solution to find all customers who never order anything.
# Return the result table in any order.
# The result format is in the following example.

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(customers, orders, left_on='id', right_on='customerId', how='left')
    df = merged_df[merged_df['customerId'].isnull()]
    df.rename(columns={'name': 'Customers'}, inplace=True)
    return df[['Customers']]

customers= pd.DataFrame()
orders= pd.DataFrame()

# Select the rows which `id` is not present in orders['customerId'].
df = customers[~customers['id'].isin(orders['customerId'])]

# Build a dataframe that only contains the column `name` 
# and rename the column `name` as `Customers`.
df = df[['name']].rename(columns={'name': 'Customers'})

import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Select the rows which `id` is not present in orders['customerId'].
    df = customers[~customers['id'].isin(orders['customerId'])]

    # Build a dataframe that only contains the column `name` 
    # and rename the column `name` as `Customers`.
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df

df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
df = df[df['customerId'].isna()]
df = df[['name']].rename(columns={'name': 'Customers'})
import pandas as pd

def customers_who_never_order(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = customers.merge(orders, left_on='id', right_on='customerId', how='left')
    df = df[df['customerId'].isna()]
    df = df[['name']].rename(columns={'name': 'Customers'})
    return df

