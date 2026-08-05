"""
Task 7: Strings & Collections
Demonstrates:
String operations: upper(), lower(), replace(), find()
List operations: append(), remove(), sort()
Tuple creation and indexing
Dictionary storing student information
Set operations: add(), remove()
"""

# ---------- String Operations ----------
text = "Python for Data Analytics"
print("----- String Operations -----")
print("Original string :", text)
print("Uppercase       :", text.upper())
print("Lowercase       :", text.lower())
print("Replace         :", text.replace("Data Analytics", "Machine Learning"))
print("Find 'Data'     : index", text.find("Data"))

# ---------- List Operations ----------
fruits = ["apple", "banana", "cherry"]
print("\n----- List Operations -----")
print("Original list   :", fruits)
fruits.append("mango")
print("After append    :", fruits)
fruits.remove("banana")
print("After remove    :", fruits)
fruits.sort()
print("After sort      :", fruits)

# ---------- Tuple ----------
coordinates = (10, 20, 30, 40)
print("\n----- Tuple -----")
print("Tuple           :", coordinates)
print("First element   :", coordinates[0])
print("Last element    :", coordinates[-1])

# ---------- Dictionary ----------
student = {
    "name": "Hrithik",
    "age": 22,
    "branch": "Computer Science",
    "cgpa": 8.7
}
print("\n----- Dictionary -----")
print("Student info    :", student)
print("Student name    :", student["name"])

# ---------- Set Operations ----------
skills = {"Python", "SQL", "Excel"}
print("\n----- Set Operations -----")
print("Original set    :", skills)
skills.add("Power BI")
print("After add       :", skills)
skills.remove("Excel")
print("After remove    :", skills)
