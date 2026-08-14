"""
Task 2: NumPy Indexing, Slicing & Reshaping
Demonstrates indexing, slicing, 2D array creation, row/column access,
and reshaping of NumPy arrays.
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])
print("----- Original Array -----")
print(arr)

# Indexing
print("\n----- Indexing -----")
print("Element at index 0 :", arr[0])
print("Element at index 5 :", arr[5])
print("Last element       :", arr[-1])

# Slicing
print("\n----- Slicing -----")
print("First 4 elements   :", arr[:4])
print("Elements 3 to 7    :", arr[3:8])
print("Every 2nd element  :", arr[::2])

# 2D array
arr_2d = arr.reshape(3, 4)
print("\n----- 2D Array (reshaped to 3x4) -----")
print(arr_2d)

# Accessing rows and columns
print("\n----- Row/Column Access -----")
print("Row 0              :", arr_2d[0])
print("Row 1               :", arr_2d[1])
print("Column 2            :", arr_2d[:, 2])
print("Element at (2, 3)   :", arr_2d[2, 3])

# Reshaping into different dimensions
reshaped_2x6 = arr.reshape(2, 6)
reshaped_4x3 = arr.reshape(4, 3)
print("\n----- Reshaping -----")
print("Original shape      :", arr.shape)
print("Reshaped to (2,6):\n", reshaped_2x6)
print("Reshaped to (4,3):\n", reshaped_4x3)
