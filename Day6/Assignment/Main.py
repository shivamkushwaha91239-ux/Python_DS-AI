#making a student management system using python

#add student 
def add_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    course = input("Enter course: ")
    email = input("Enter email: ")
    college = input("Enter college: ")
    return {"name": name, "age": age, "course": course, "email": email, "college": college}

#view student 
def view_students(students):
    if not students:
        print("No students found.")
    else:
        for i, student in enumerate(students):
            print(f"Student {i+1}:")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Email: {student['email']}")
            print(f"College: {student['college']}")
            print()
# search student 
def search_student(students):
    name = input("Enter name to search: ")
    found_students = [student for student in students if student['name'].lower() == name.lower()]
    if not found_students:
        print("No students found with that name.")
    else:
        for student in found_students:
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Email: {student['email']}")
            print(f"College: {student['college']}")
            print()            
#delete student
def delete_student(students):
    name = input("Enter name to delete: ")
    for i, student in enumerate(students):
        if student['name'].lower() == name.lower():
            del students[i]
            print(f"Student {name} deleted.")
            return
    print("No students found with that name.")

#update student
def update_student(students):
    name = input("Enter name to update: ")
    for student in students:
        if student['name'].lower() == name.lower():
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"Name ({student['name']}): ") or student['name']
            new_age = input(f"Age ({student['age']}): ") or student['age']
            new_course = input(f"Course ({student['course']}): ") or student['course']
            new_email = input(f"Email ({student['email']}): ") or student['email']
            new_college = input(f"College ({student['college']}): ") or student['college']
            
            student.update({
                "name": new_name,
                "age": int(new_age),
                "course": new_course,
                "email": new_email,
                "college": new_college
            })
            print(f"Student {name} updated.")
            return
    print("No students found with that name.")

    # menu for student management system
def menu():
    students = []
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Update Student")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student = add_student()
            students.append(student)
            print("Student added successfully.")
        elif choice == '2':
            view_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '5':
            update_student(students)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")