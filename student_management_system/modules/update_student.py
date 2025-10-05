from student_management_system.student_data import students, VALID_COURSES
from student_management_system.modules.export_data import export_students_to_csv

def update_student():
    if not students:
        print("\n⚠️ No students available to update.")
        return

    student_id = input("Enter Student ID to update: ").strip()
    target = next((s for s in students if s['id'] == student_id), None)

    if target:
        print(f"Found student: {target['name']}")
        choice = input("Update (course/marks): ").lower()

        if choice == 'course':
            while True:
                new_course = input(f"Enter new course ({', '.join(VALID_COURSES)}): ").upper()
                if new_course in VALID_COURSES:
                    target['course'] = new_course
                    print("✅ Success: Course updated.")
                    export_students_to_csv()  # Save after update
                    break
                else:
                    print("⚠️ Invalid course.")

        elif choice == 'marks':
            while True:
                try:
                    new_marks = int(input("Enter new marks: "))
                    target['marks'] = new_marks
                    print("✅ Success: Marks updated.")
                    export_students_to_csv()  # Save after update
                    break
                except ValueError:
                    print("⚠️ Enter a number.")

        else:
            print("⚠️ Invalid choice. Choose 'course' or 'marks'.")
    else:
        print(f"⚠️ No student with ID '{student_id}' found.")