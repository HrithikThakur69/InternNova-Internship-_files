"""
Task 9: Exporting Data
Processes the students dataset (fills missing values, adds a grade column)
and exports the final DataFrame to a new CSV file, then verifies the export.
"""

import pandas as pd

df = pd.read_csv("students.csv")

# Process the data: fill missing values and add a grade column
df["Marks"] = df["Marks"].fillna(round(df["Marks"].mean(), 1))
df["Attendance"] = df["Attendance"].fillna(round(df["Attendance"].mean(), 1))
df["Grade"] = df["Marks"].apply(lambda m: "A" if m >= 85 else "B" if m >= 70 else "C")

output_file = "students_processed.csv"
df.to_csv(output_file, index=False)
print(f"Processed data exported to '{output_file}'.\n")

# Verify the exported file
verify_df = pd.read_csv(output_file)
print("----- Verifying Exported File -----")
print(f"Rows: {verify_df.shape[0]}, Columns: {verify_df.shape[1]}")
print("\n----- Contents of Exported CSV -----")
print(verify_df)
