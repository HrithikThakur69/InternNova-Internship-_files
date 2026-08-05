"""
Task 6: Functions
Two user-defined functions:
1. Function to calculate the square of a number.
2. Function to calculate the average of three numbers.
Both functions are called with user input.
"""


def calculate_square(number):
    """Returns the square of a given number."""
    return number ** 2


def calculate_average(a, b, c):
    """Returns the average of three numbers."""
    return (a + b + c) / 3


# --- Using the functions ---
num = int(input("Enter a number to find its square: "))
print(f"Square of {num} = {calculate_square(num)}")

n1 = int(input("\nEnter first number: "))
n2 = int(input("Enter second number: "))
n3 = int(input("Enter third number: "))
print(f"Average of {n1}, {n2}, {n3} = {calculate_average(n1, n2, n3)}")
