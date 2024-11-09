# Example of a list of dictionaries
students = [
    {"name": "Amal", "age": 22, "major": "Physics"},
    {"name": "Maimoona", "age": 22, "major": "Mathematics"},
    {"name": "Maria", "age": 21, "major": "Computer Science"}
]

# Accessing each dictionary in the list
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Major: {student['major']}")

# Adding a new dictionary to the list
new_student = {"name": "Daisy", "age": 23, "major": "Chemistry"}
students.append(new_student)

print("\nUpdated list of students:")
for student in students:
    print(student)
