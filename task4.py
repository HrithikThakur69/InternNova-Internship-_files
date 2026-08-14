"""
Task 4: Pandas Series & DataFrame
Creates a Pandas Series, a DataFrame with student information,
displays column names/index, and adds a new column.
"""

import pandas as pd

# Pandas Series
marks_series = pd.Series([88, 76, 65, 91, 58], name="marks")
print("----- Pandas Series -----")
print(marks_series)

# DataFrame with student information
data = {
    "student_id": [101, 102, 103, 104, 105],
    "name": ["Aarav Sharma", "Priya Verma", "Rohan Gupta", "Sneha Iyer", "Karan Mehta"],
    "branch": ["CSE", "ECE", "CSE", "ME", "ECE"],
    "marks": [88, 76, 65, 91, 58]
}
df = pd.DataFrame(data)

print("\n----- Student DataFrame -----")
print(df)

print("\n----- Column Names -----")
print(df.columns.tolist())

print("\n----- Index -----")
print(df.index)

# Adding a new column
df["grade"] = df["marks"].apply(lambda m: "A" if m >= 85 else "B" if m >= 70 else "C")

print("\n----- Updated DataFrame (with 'grade' column) -----")
print(df)
