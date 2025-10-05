from student_management_system.student_data import students, VALID_COURSES, MAX_STUDENTS
from student_management_system.modules.export_data import export_students_to_csv
"""
add_student.py
--------------
Handles adding new students to the system.
"""
def add_student():
    """Prompts user for student details and adds a new student to the list."""
    if len(students) >= MAX_STUDENTS:
        print("⚠️ Error: Maximum student limit reached (8).")
        return

    print("\nEnter New Student Details:")
    student_id = input("Enter Student ID: ").strip()
    if not student_id:
        print("⚠️ Error: Student ID cannot be empty.")
    elif any(s['id'] == student_id for s in students):
        print("⚠️ Error: Student ID already exists.")
        
        return
    name = input("Enter Student Name: ").strip()

    while True:
        course = input(f"Enter Course ({', '.join(VALID_COURSES)}): ").upper()
        if course in VALID_COURSES:
            break
        else:
            print(f"Invalid course. Please choose from: {', '.join(VALID_COURSES)}")

    while True:
        try:
            marks = int(input("Enter Marks(0-100): "))
            if 0 <= marks <= 100:
                break
            else:
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(new_student)
    export_students_to_csv()  # <-- Save after adding
    print("✅ Success: Student added successfully!")