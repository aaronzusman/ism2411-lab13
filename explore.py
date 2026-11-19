
# ISM2411 Lab 13 - First DataFrame - Retail Sales Explorer
# Name: Aaron Zusman
#
# SELF-ASSESSMENT
#
# 1. A boolean filter checks whether rows meet a certain condition.
#    It only returns the rows where the condition is True.
#
# 2. df["revenue"] selects one column as a Series.
#    df[["revenue"]] selects one column as a DataFrame.
#    This matters when working with functions that require a DataFrame.
#
# 3. Pandas makes it easier to organize, filter, and analyze large
#    amounts of data quickly. It also makes the process repeatable.
#
# --------------------------------------------------
# EXERCISE 1 - LOAD IT
# --------------------------------------------------

import pandas as pd
import os

df = pd.read_csv('data/retail_sales.csv')

print("EXERCISE 1 - LOAD IT")
print(df.head())
print(df.shape)
print(df.columns.tolist())
print(df.dtypes)


# --------------------------------------------------
# EXERCISE 2 - FILTER BY REGION
# --------------------------------------------------

print("\nEXERCISE 2 - FILTER BY REGION")

south = df[df['region'] == 'South']

print(len(south))
print(south.head())


# --------------------------------------------------
# EXERCISE 3 - TOP 5 BY REVENUE
# --------------------------------------------------

print("\nEXERCISE 3 - TOP 5 BY REVENUE")

top_revenue = df.sort_values('revenue', ascending=False).head(5)

print(top_revenue)


# --------------------------------------------------
# EXERCISE 4 - TWO-CONDITION FILTER
# --------------------------------------------------

print("\nEXERCISE 4 - TWO-CONDITION FILTER")

big_south = df[(df['region'] == 'South') & (df['revenue'] > 1000)]

print(len(big_south))
print(big_south.head())


# --------------------------------------------------
# EXERCISE 5 - A NEW COLUMN
# --------------------------------------------------

print("\nEXERCISE 5 - A NEW COLUMN")

df['per_unit'] = df['revenue'] / df['quantity']

print(df.head())
print(df['per_unit'].mean())


# --------------------------------------------------
# EXERCISE 6 - UNIQUE VALUES
# --------------------------------------------------

print("\nEXERCISE 6 - UNIQUE VALUES")

print(df['region'].unique())
print(df['region'].value_counts())


# --------------------------------------------------
# EXERCISE 7 - SELECT COLUMNS
# --------------------------------------------------

print("\nEXERCISE 7 - SELECT COLUMNS")

selected_columns = df[['region', 'product', 'revenue']]

print(selected_columns.shape)


# --------------------------------------------------
# EXERCISE 8 - SAVE
# --------------------------------------------------

print("\nEXERCISE 8 - SAVE")

df.to_csv('data/explored.csv', index=False)

print(os.path.exists('data/explored.csv'))
