"""
menu.py
-------
Handles displaying the menu and routing choices to student service functions.
"""
from student_management_system.modules.console_ui import print_menu, print_students_table, print_message
from student_management_system.modules.export_data import export_students_to_csv
from student_management_system.modules.import_data import import_students_from_csv
from student_management_system.modules.add_student import add_student
from student_management_system.modules.view_students import view_students
from student_management_system.modules.search_student import search_student
from student_management_system.modules.update_student import update_student
from student_management_system.modules.delete_student import delete_student

def menu():
    while True:
        print_menu()

        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            search_student()
        elif choice == '4':
            update_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            export_students_to_csv()
        elif choice == '7':
            import_students_from_csv()
        elif choice == '8':
            print_message("👋 Thank you for using the system. Exiting.", style="cyan")
            break
        else:
            print_message("⚠️ Invalid choice. Please enter a number between 1 and 8.", style="yellow")