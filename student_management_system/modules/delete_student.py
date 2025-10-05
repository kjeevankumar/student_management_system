from student_management_system.student_data import students
from student_management_system.modules.export_data import export_students_to_csv

def delete_student():
    if not students:
        print("\n⚠️ No students available to delete.")
        return

    student_id = input("Enter Student ID to delete: ").strip()
    target = next((s for s in students if s['id'] == student_id), None)

    if target:
        students.remove(target)
        export_students_to_csv()  # Save after delete
        print(f"✅ Success: Student '{target['name']}' deleted.")
    else:
        print(f"⚠️ No student with ID '{student_id}' found.")