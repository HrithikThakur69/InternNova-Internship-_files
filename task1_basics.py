"""
Task 1: Python Basics
Prints a welcome message
Takes your Name, College Name, and Branch as input,
then displays the entered information in a formatted output.
"""

print("Welcome to Python Programming for Data Analytics!")
print("-----------------------------------------------")

name = input("Enter your Name: ")
college = input("Enter your College Name: ")
branch = input("Enter your Branch: ")

print("\n----- Student Details -----")
print(f"Name          : {name}")
print(f"College Name  : {college}")
print(f"Branch        : {branch}")
print("----------------------------")
