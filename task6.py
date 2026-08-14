"""
Task 6: Selecting, Filtering & Sorting Data
Demonstrates selecting columns/rows, filtering with single and multiple
conditions, and sorting a DataFrame in ascending and descending order.
"""

import pandas as pd

df = pd.read_csv("students.csv")

# Select specific columns
print("----- Selecting Specific Columns (name, marks) -----")
print(df[["Name", "Marks"]])

# Select specific rows
print("\n----- Selecting Specific Rows (index 0 to 3) -----")
print(df.iloc[0:4])

# Filter based on a single condition
print("\n----- Students with marks > 80 -----")
print(df[df["Marks"] > 80])

# Multiple filtering conditions
print("\n----- CSE Students with marks > 70 -----")
print(df[(df["Branch"] == "CSE") & (df["Marks"] > 70)])

# Sort ascending
print("\n----- Sorted by marks (Ascending) -----")
print(df.sort_values(by="Marks", ascending=True))

# Sort descending
print("\n----- Sorted by marks (Descending) -----")
print(df.sort_values(by="Marks", ascending=False))
