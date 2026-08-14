"""
Task 1: NumPy Introduction & Arrays
Creates a NumPy array of at least 10 numbers, displays it along with its
shape, size, and data type, and creates 1D and 2D arrays.
"""

import numpy as np

# 1D array with at least 10 numbers
arr = np.array([12, 45, 7, 23, 56, 89, 34, 21, 67, 90, 15])

print("----- 1D NumPy Array -----")
print("Array          :", arr)
print("Shape          :", arr.shape)
print("Size           :", arr.size)
print("Data type      :", arr.dtype)

# One-dimensional array
one_d = np.array([1, 2, 3, 4, 5])
print("\n----- One-Dimensional Array -----")
print(one_d)
print("Shape:", one_d.shape)

# Two-dimensional array
two_d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("\n----- Two-Dimensional Array -----")
print(two_d)
print("Shape:", two_d.shape)
