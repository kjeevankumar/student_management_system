from student_management_system.student_data import students

def search_student():
    if not students:
        print("\n⚠️ No students found.")
        return

    search_term = input("Enter Student ID or Name: ").strip()
    found = [s for s in students if search_term == s['id'] or search_term.lower() in s['name'].lower()]

    if found:
        print("\n--- Search Results ---")
        print(f"{'ID':<10} {'Name':<20} {'Course':<10} {'Marks':<10}")
        print("-" * 50)
        for s in found:
            print(f"{s['id']:<10} {s['name']:<20} {s['course']:<10} {s['marks']:<10}")
        print("-" * 50)
    else:
        print(f"⚠️ No student found with '{search_term}'.")