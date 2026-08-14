"""
Task 8: Merge, Concatenate, GroupBy & Pivot Table
Uses students.csv and departments.csv to demonstrate merging, concatenation,
GroupBy aggregation, and Pivot Table creation.
"""

import pandas as pd

students = pd.read_csv("students.csv")
departments = pd.read_csv("departments.csv")

print("----- Students Dataset -----")
print(students)

print("\n----- Departments Dataset -----")
print(departments)

# Merge on the common column 'branch'
merged = pd.merge(students, departments, on="Branch", how="left")
print("\n----- Merged DataFrame (students + departments on 'Branch') -----")
print(merged[["Student_id", "Name", "Branch", "HOD", "Building"]])

# Concatenate two DataFrames (splitting students into two halves as an example)
first_half = students.iloc[:7]
second_half = students.iloc[7:]
concatenated = pd.concat([first_half, second_half], ignore_index=True)
print("\n----- Concatenated DataFrame (two halves of students) -----")
print(concatenated)

# GroupBy: group by branch and calculate aggregate marks
print("\n----- GroupBy: Average, Count, Min, Max Marks per Branch -----")
grouped = students.groupby("Branch")["Marks"].agg(["mean", "count", "min", "max"])
print(grouped)

# Pivot Table: average marks and attendance per branch and city
print("\n----- Pivot Table: Average Marks by Branch and City -----")
pivot = pd.pivot_table(
    students,
    values="Marks",
    index="Branch",
    columns="City",
    aggfunc="mean"
)
print(pivot)
