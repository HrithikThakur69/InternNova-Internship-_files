"""
Task 4: Conditional Statements
Takes marks as input and displays the grade using if, elif, and else.
Grading scheme: 90+ -> A, 75-89 -> B, 60-74 -> C, Below 60 -> Fail
"""

marks = int(input("Enter your marks: "))

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"\nMarks obtained : {marks}")
print(f"Grade          : {grade}")
