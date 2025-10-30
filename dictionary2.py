# A list to store multiple students
students = []

print("=== Student Information System ===")

# Let user add multiple students
while True:
    name = input("\nEnter student name (or type 'stop' to finish): ")
    if name.lower() == "stop":
        break
    
    age = int(input("Enter student age: "))
    
    # Collect multiple subjects
    subjects = []
    print("Enter subjects one by one (type 'done' when finished):")
    while True:
        subject = input("Subject: ")
        if subject.lower() == "done":
            break
        subjects.append(subject)
    
    # Create a dictionary for the student
    student = {
        "name": name,
        "age": age,
        "subjects": subjects
    }
    
    # Add to the students list
    students.append(student)

# Show all students
print("\n=== All Students ===")
for student in students:
    print(f"Name: {student['name']}, Age: {student['age']}, Subjects: {', '.join(student['subjects'])}")

# Example: Find students by subject
search_subject = input("\nEnter a subject to find students enrolled: ")
print(f"\nStudents taking {search_subject}:")
found = False
for student in students:
    if search_subject in student["subjects"]:
        print(student["name"])
        found = True

if not found:
    print("No students found for this subject.")
