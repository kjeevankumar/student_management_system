import csv
from student_management_system.student_data import students

def export_students_to_csv(filename="students.csv"):
    if not students:
        print("⚠️ No students to export.")
        return
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["id", "name", "course", "marks"])
        writer.writeheader()
        writer.writerows(students)
    print(f"✅ Students exported to {filename}")