"""
Task 8: Basic File Handling
Creates a text file, writes an introduction into it,
then reads and displays the file contents.
"""

file_name = "introduction.txt"

introduction = (
    "Hi, my name is Hrithik Thakur. A.\n"
    "I am a Computer Science student passionate about Data Analytics.\n"
    "I enjoy working with Python, SQL, and data visualization tools.\n"
)

# Writing to the file
with open(file_name, "w") as file:
    file.write(introduction)
print(f"File '{file_name}' created and introduction written successfully.\n")

# Reading from the file
with open(file_name, "r") as file:
    content = file.read()

print("----- File Contents -----")
print(content)
