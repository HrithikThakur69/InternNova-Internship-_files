"""
Task 5: Loops
1. Print numbers from 1 to 20 using a for loop.
2. Print the multiplication table of a number entered by the user.
3. Print even numbers from 1 to 50 using a while loop.
"""

# 1. Numbers from 1 to 20 using a for loop
print("Numbers from 1 to 20:")
for i in range(1, 21):
    print(i, end=" ")
print("\n")

# 2. Multiplication table using any number
num = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# 3. Even numbers from 1 to 50 using a while loop
print("\nEven numbers from 1 to 50:")
n = 1
while n <= 50:
    if n % 2 == 0:
        print(n, end=" ")
    n += 1
print()
