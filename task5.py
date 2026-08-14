"""
Task 5: Reading & Inspecting Data
Reads students.csv using Pandas and inspects it using head(), tail(),
shape, columns, dtypes, info(), and describe().
"""

import pandas as pd

df = pd.read_csv("students.csv")

print("----- First 5 Rows (head) -----")
print(df.head())

print("\n----- Last 5 Rows (tail) -----")
print(df.tail())

print("\n----- Shape (rows, columns) -----")
print(df.shape)

print("\n----- Column Names -----")
print(df.columns.tolist())

print("\n----- Data Types -----")
print(df.dtypes)

print("\n----- info() -----")
df.info()

print("\n----- describe() -----")
print(df.describe())
