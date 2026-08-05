"""
Task 9: Mini Python Project - Student Record Management System
Allows the user to Add, Display, Search, and Delete student records.
Records are stored as a list of dictionaries.
"""

students = []  # each record: {"name": ..., "roll_no": ..., "branch": ..., "marks": ...}

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    branch = input("Enter branch: ")
    marks = input("Enter marks: ")
    student = {"name": name, "roll_no": roll_no, "branch": branch, "marks": marks}
    students.append(student)
    print(f"Student '{name}' added successfully.\n")

def display_students():
    if not students:
        print("No student records found.\n")
        return
    print("\n----- All Student Records -----")
    for idx, s in enumerate(students, start=1):
        print(f"{idx}. Name: {s['name']}, Roll No: {s['roll_no']}, "
              f"Branch: {s['branch']}, Marks: {s['marks']}")
    print()


def search_student(name):
    found = [s for s in students if s["name"].lower() == name.lower()]
    if found:
        print(f"\nRecord(s) found for '{name}':")
        for s in found:
            print(s)
    else:
        print(f"\nNo record found for '{name}'.")
    print()


def delete_student(name):
    global students
    before = len(students)
    students = [s for s in students if s["name"].lower() != name.lower()]
    if len(students) < before:
        print(f"\nRecord for '{name}' deleted successfully.\n")
    else:
        print(f"\nNo record found for '{name}' to delete.\n")


def menu():
    while True:
        print("===== Student Record Management System =====")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student by Name")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            name = input("Enter name to search: ")
            search_student(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            delete_student(name)
        elif choice == "5":
            print("Exiting Student Record Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    menu()
