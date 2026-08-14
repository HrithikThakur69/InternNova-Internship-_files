"""
Task 10: Mini Data Analysis Project
Dataset: Student Performance Dataset (students.csv)

Performs an end-to-end mini analysis: loading, inspection, missing-value
handling, filtering, sorting, GroupBy analysis, a Pivot Table, insight
extraction, data visualization, and exporting the cleaned dataset.
"""

import pandas as pd
import matplotlib
matplotlib.use("Agg")  # render to file instead of opening a window
import matplotlib.pyplot as plt

# 1. Loading the dataset
df = pd.read_csv("students.csv")
print("----- 1. Dataset Loaded -----")
print(df)

# 2. Data inspection
print("\n----- 2. Data Inspection -----")
print("Shape:", df.shape)
print(df.info())
print(df.describe())

# 3. Identifying and handling missing values
print("\n----- 3. Missing Values -----")
print(df.isnull().sum())
df["Marks"] = df["Marks"].fillna(round(df["Marks"].mean(), 1))
df["Attendance"] = df["Attendance"].fillna(round(df["Attendance"].mean(), 1))
print("\nMissing values handled by filling with column mean.")
print(df.isnull().sum())

# 4. Selecting and filtering data
print("\n----- 4. Filtering: Students with marks >= 75 -----")
high_performers = df[df["Marks"] >= 75]
print(high_performers[["Name", "Branch", "Marks"]])

# 5. Sorting data
print("\n----- 5. Sorting by Marks (Descending) -----")
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df[["Name", "Branch", "Marks"]])

# 6. GroupBy analysis
print("\n----- 6. GroupBy: Branch-wise Performance -----")
branch_summary = df.groupby("Branch").agg(
    avg_marks=("Marks", "mean"),
    avg_attendance=("Attendance", "mean"),
    total_students=("Student_id", "count")
).round(2)
print(branch_summary)

# 7. Pivot Table
print("\n----- 7. Pivot Table: Average Marks by Branch and City -----")
pivot = pd.pivot_table(df, values="Marks", index="Branch", columns="City", aggfunc="mean")
print(pivot)

# 8. Insights
top_branch = branch_summary["avg_marks"].idxmax()
top_student = df.loc[df["Marks"].idxmax()]
low_attendance_count = (df["Attendance"] < 80).sum()

print("\n----- 8. Key Insights -----")
print(f"- The branch with the highest average marks is '{top_branch}' "
      f"({branch_summary.loc[top_branch, 'avg_marks']} avg marks).")
print(f"- The top-scoring student is '{top_student['Name']}' from {top_student['Branch']} "
      f"with {top_student['Marks']} marks.")
print(f"- {low_attendance_count} student(s) have attendance below 80%, "
      f"which may correlate with lower performance.")
print(f"- Overall average marks across all students: {round(df['Marks'].mean(), 2)}")

# 9. Visualizations
print("\n----- 9. Generating Visualizations -----")

plt.style.use("seaborn-v0_8-whitegrid")

# Chart 1: Average marks by branch (bar chart)
fig, ax = plt.subplots(figsize=(6, 4))
branch_summary["avg_marks"].plot(kind="bar", color="#2E8B57", ax=ax)
ax.set_title("Average Marks by Branch")
ax.set_xlabel("Branch")
ax.set_ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart1_avg_marks_by_branch.png", dpi=150)
plt.close()

# Chart 2: Average attendance by branch (bar chart)
fig, ax = plt.subplots(figsize=(6, 4))
branch_summary["avg_attendance"].plot(kind="bar", color="#4682B4", ax=ax)
ax.set_title("Average Attendance by Branch")
ax.set_xlabel("Branch")
ax.set_ylabel("Average Attendance (%)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart2_avg_attendance_by_branch.png", dpi=150)
plt.close()

# Chart 3: Distribution of marks (histogram)
fig, ax = plt.subplots(figsize=(6, 4))
ax.hist(df["Marks"], bins=6, color="#CD853F", edgecolor="black")
ax.set_title("Distribution of Student Marks")
ax.set_xlabel("Marks")
ax.set_ylabel("Number of Students")
plt.tight_layout()
plt.savefig("chart3_marks_distribution.png", dpi=150)
plt.close()

# Chart 4: Marks vs Attendance (scatter plot, colored by branch)
fig, ax = plt.subplots(figsize=(6, 4))
colors = {"CSE": "#e74c3c", "ECE": "#3498db", "ME": "#2ecc71"}
for branch, group in df.groupby("Branch"):
    ax.scatter(group["Attendance"], group["Marks"], label=branch,
               color=colors.get(branch, "gray"), s=60, edgecolor="black")
ax.set_title("Marks vs Attendance")
ax.set_xlabel("Attendance (%)")
ax.set_ylabel("Marks")
ax.legend(title="Branch")
plt.tight_layout()
plt.savefig("chart4_marks_vs_attendance.png", dpi=150)
plt.close()

print("4 charts saved:")
print(" - chart1_avg_marks_by_branch.png")
print(" - chart2_avg_attendance_by_branch.png")
print(" - chart3_marks_distribution.png")
print(" - chart4_marks_vs_attendance.png")

# 10. Exporting the cleaned/processed dataset
output_file = "students_final_cleaned.csv"
df.to_csv(output_file, index=False)
print(f"\nCleaned dataset exported to '{output_file}'.")
