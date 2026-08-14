"""
Task 3: NumPy Mathematical & Statistical Operations
Performs basic arithmetic operations and statistical functions
on a numerical dataset representing students' marks.
"""

import numpy as np

marks_a = np.array([88, 76, 65, 91, 58, 73, 84, 95, 69, 80])
marks_b = np.array([5, 4, 3, 6, 2, 4, 5, 3, 4, 2])  # bonus marks

print("----- Dataset -----")
print("Marks A (exam) :", marks_a)
print("Marks B (bonus):", marks_b)

# Mathematical operations
print("\n----- Mathematical Operations -----")
print("Addition       :", marks_a + marks_b)
print("Subtraction    :", marks_a - marks_b)
print("Multiplication :", marks_a * marks_b)
print("Division       :", np.round(marks_a / marks_b, 2))

# Statistical functions
print("\n----- Statistical Functions (Marks A) -----")
print("Mean           :", np.mean(marks_a))
print("Median         :", np.median(marks_a))
print("Minimum        :", np.min(marks_a))
print("Maximum        :", np.max(marks_a))
print("Standard Dev.  :", round(np.std(marks_a), 2))
print("Sum            :", np.sum(marks_a))
