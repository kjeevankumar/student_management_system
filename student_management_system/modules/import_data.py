import csv
from student_management_system.student_data import students

def import_students_from_csv(filename="students.csv"):
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            students.clear()
            for row in reader:
                row['marks'] = int(row['marks'])
                students.append(row)
        print(f"✅ Students imported from {filename}")
    except FileNotFoundError:
        print(f"⚠️ File {filename} not found.")