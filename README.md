# Student Management System 🎓

![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue)

A comprehensive, command-line (CLI) application for managing student records. This system is built with a highly modular architecture in Python and features persistent data storage using a CSV file, ensuring that no data is lost between sessions. It includes full CRUD (Create, Read, Update, Delete) functionality as well as data import and export capabilities.

## 🌟 Key Features

-   **Full CRUD Operations**: Add, view, search, update, and delete student records.
-   **Persistent Data Storage**: All student records are automatically saved to and loaded from a `students.csv` file.
-   **CSV Import & Export**:
    -   **Import**: Bulk-add students to the system by importing from a CSV file.
    -   **Export**: Save the current list of all students to a new CSV file for reporting or backup.
-   **Modular Codebase**: Each core feature is separated into its own Python module, making the code clean, organized, and easy to maintain.
-   **Interactive CLI**: A user-friendly menu for navigating the system's features.

## 📸 Demo

A quick demonstration of the main menu and functionality:

```text
===== Student Management System =====
1. Add Student
2. View All Students
3. Search for a Student
4. Update Student Information
5. Delete a Student
6. Import data from CSV
7. Export data to CSV
8. Exit
Enter your choice (1-8): 2

ID         Name                 Course     Marks     
--------------------------------------------------
1          Ravi Kumar           CSE        85        
2          Priya Sharma         ECE        92        
3          Suresh Singh         MECH       78        
--------------------------------------------------
📂 Project Structure
The application is broken down into feature-specific modules for maximum organization:

.
├── students.csv            # The primary data storage file
├── console_ui.py           # The main entry point and user interface
|
├── add_student.py          # Logic for adding new students
├── view_students.py        # Logic for displaying student records
├── search_student.py       # Logic for finding a specific student
├── update_student.py       # Logic for modifying student records
├── delete_student.py       # Logic for removing students
|
├── import_data.py          # Logic for importing from CSV
├── export_data.py          # Logic for exporting to CSV
└── README.md               # This documentation file
⚙️ Setup and Installation
This project is built using Python's standard libraries, so no special installation of external packages is required.

1. Clone the Repository

Bash

# Replace 'your-github-username' with your actual username
git clone [https://github.com/your-github-username/student-management-system.git](https://github.com/your-github-username/student-management-system.git)
cd student-management-system
2. The students.csv file
The application will automatically create a students.csv file in the same directory if one does not exist when you first add a student. The expected format for the CSV header is: ID,Name,Course,Marks.

▶️ How to Run
To start the application, run the console_ui.py file from your terminal:

Bash

python console_ui.py
This will launch the main menu, and from there you can access all the features of the system.

🛠️ Technologies Used
Python 3.8+

Standard Libraries:

csv: For reading from and writing to the CSV data file.

os: For checking file existence.