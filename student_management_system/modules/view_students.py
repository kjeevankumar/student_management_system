from student_management_system.student_data import students

def view_students():
    import os
    #os.system('cls')
    if not students:
        
        print("\n⚠️ No students found. The list is empty.")
        return

    print("\n--- All Student Records ---")
    print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Marks':<10}")
    print("-" * 50)
    for s in students:
        print(f"{s['id']:<10} {s['name']:<20} {s['course']:<10} {s['marks']:<10}")
    print("-" * 50)