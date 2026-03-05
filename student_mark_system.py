# Student Mark Management System

students = []

while True:
    print("\n----- STUDENT MARK SYSTEM -----")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter student name: ")

        m1 = float(input("Enter marks for Subject 1: "))
        m2 = float(input("Enter marks for Subject 2: "))
        m3 = float(input("Enter marks for Subject 3: "))

        total = m1 + m2 + m3
        percentage = total / 3

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "Fail"

        student = {
            "name": name,
            "total": total,
            "percentage": percentage,
            "grade": grade
        }

        students.append(student)

        print("Student added successfully!")

    elif choice == 2:
        print("\nStudent Results:")
        for s in students:
            print("Name:", s["name"])
            print("Total:", s["total"])
            print("Percentage:", s["percentage"])
            print("Grade:", s["grade"])
            print("----------------------")

    elif choice == 3:
        print("Program ended")
        break

    else:
        print("Invalid choice")