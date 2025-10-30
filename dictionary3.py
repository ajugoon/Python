# Student Information System using Lists and Dictionaries

students = []  # List to hold all student dictionaries

def add_student():
    """Add a new student"""
    name = input("\nEnter student name: ")
    age = int(input("Enter student age: "))
    
    subjects = []
    print("Enter subjects one by one (type 'done' when finished):")
    while True:
        subject = input("Subject: ")
        if subject.lower() == "done":
            break
        subjects.append(subject)
    
    student = {
        "name": name,
        "age": age,
        "subjects": subjects
    }
    students.append(student)
    print(f"✅ Student '{name}' added successfully!")


def view_students():
    """View all students"""
    if not students:
        print("\nNo students available yet.")
        return
    print("\n=== All Students ===")
    for i, student in enumerate(students, start=1):
        print(f"{i}. Name: {student['name']}, Age: {student['age']}, Subjects: {', '.join(student['subjects'])}")


def search_by_subject():
    """Find students by subject"""
    if not students:
        print("\nNo students available yet.")
        return
    subject = input("\nEnter subject to search for: ")
    found = [s["name"] for s in students if subject in s["subjects"]]
    
    if found:
        print(f"\nStudents taking {subject}: {', '.join(found)}")
    else:
        print(f"\nNo students found for subject '{subject}'.")


# === Main Menu ===
while True:
    print("\n===== Student Information Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Students by Subject")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_by_subject()
    elif choice == "4":
        print("\nExiting program. Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Please try again.")
