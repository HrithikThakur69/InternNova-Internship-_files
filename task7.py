"""
Task 7: Handling Missing Values
Identifies, counts, removes, and fills missing values in the dataset,
and shows the DataFrame before and after handling missing data.
"""

import pandas as pd

df = pd.read_csv("students.csv")

print("----- Dataset Before Handling Missing Values -----")
print(df)

# Identify missing values
print("\n----- Missing Values (True/False) -----")
print(df.isnull())

# Count missing values per column
print("\n----- Count of Missing Values per Column -----")
print(df.isnull().sum())

# Remove rows containing missing values
df_dropped = df.dropna()
print("\n----- Dataset After Dropping Rows with Missing Values -----")
print(df_dropped)

# Fill missing values (numeric columns filled with column mean)
df_filled = df.copy()
df_filled["Marks"] = df_filled["Marks"].fillna(round(df_filled["Marks"].mean(), 1))
df_filled["Attendance"] = df_filled["Attendance"].fillna(round(df_filled["Attendance"].mean(), 1))

print("\n----- Dataset After Filling Missing Values (with column mean) -----")
print(df_filled)

print("""
----- Why Handling Missing Data Matters in Data Analytics -----
Missing values can distort statistical calculations (mean, sum, correlations),
break machine learning models that cannot handle NaN values, and lead to biased
or incorrect conclusions if ignored. Properly identifying and handling missing
data (via removal or imputation) ensures the dataset remains accurate, complete,
and reliable for further analysis and decision-making.
""")
