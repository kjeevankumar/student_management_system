"""
main.py
-------
Entry point of the Student Management System.
"""

from student_management_system.utils.menu import menu
from student_management_system.modules.import_data import import_students_from_csv

def main():
    """Runs the main application loop."""
    import_students_from_csv()  # Load previous data at startup
    menu()

if __name__ == "__main__":
    main()