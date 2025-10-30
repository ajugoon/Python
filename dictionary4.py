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


def update_student():
    """Update student details"""
    view_students()
    if not students:
        return
    try:
        choice = int(input("\nEnter the student number to update: "))
        if 1 <= choice <= len(students):
            student = students[choice - 1]
            print(f"\nUpdating student: {student['name']}")
            
            new_name = input("Enter new name (leave blank to keep current): ")
            if new_name:
                student["name"] = new_name
            
            new_age = input("Enter new age (leave blank to keep current): ")
            if new_age:
                student["age"] = int(new_age)
            
            print("Enter new subjects (type 'done' when finished, leave blank to keep current):")
            new_subjects = []
            while True:
                subject = input("Subject: ")
                if subject.lower() == "done":
                    break
                elif subject == "":
                    new_subjects = student["subjects"]  # Keep existing if blank
                    break
                else:
                    new_subjects.append(subject)
            student["subjects"] = new_subjects

            print("✅ Student updated successfully!")
        else:
            print("❌ Invalid student number.")
    except ValueError:
        print("❌ Please enter a valid number.")


def remove_student():
    """Remove a student"""
    view_students()
    if not students:
        return
    try:
        choice = int(input("\nEnter the student number to remove: "))
        if 1 <= choice <= len(students):
            removed = students.pop(choice - 1)
            print(f"🗑️ Student '{removed['name']}' removed successfully!")
        else:
            print("❌ Invalid student number.")
    except ValueError:
        print("❌ Please enter a valid number.")


# === Main Menu ===
while True:
    print("\n===== Student Information Menu =====")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Students by Subject")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_by_subject()
    elif choice == "4":
        update_student()
    elif choice == "5":
        remove_student()
    elif choice == "6":
        print("\nExiting program. Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Please try again.")
