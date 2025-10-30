# A list to store multiple students
students = []

# Adding students as dictionaries
student1 = {
    "name": "Alice",
    "age": 15,
    "subjects": ["Math", "Science", "English"]
}

student2 = {
    "name": "Bob",
    "age": 16,
    "subjects": ["History", "Math", "Art"]
}

student3 = {
    "name": "Charlie",
    "age": 15,
    "subjects": ["Science", "Geography", "Music"]
}

# Append each student dictionary to the list
students.append(student1)
students.append(student2)
students.append(student3)

# Print all students
print("All Students:")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Subjects: {', '.join(student['subjects'])}")

# Example: find all students taking Math
print("\nStudents taking Math:")
for student in students:
    if "Math" in student["subjects"]:
        print(student["name"])
