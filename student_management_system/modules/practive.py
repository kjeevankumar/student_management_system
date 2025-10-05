from student_management_system.student_data import students , VALID_COURSES,MAX_STUDENTS
def add_student():
  if len(students) >=max_students:
    print("maximum students limit reacheed")
    return 
  else:
    student_id=input("enter student id").strip()
    if not student_id:
      print("student idcan;t be empty ")
    elif any(s["id"]==student_id for s in students):
      print("student id can;t be same")
      return
    name=input("enter student name ").strip()

    while True:  #for running a loop until valid input is given from user side
      course=input(f" chose your course {', '.join(VALID_COURSES)}").upper()
      if course in VALID_COURSES:
        break
      else:
        print(f"invalid course please choose from {', '.join(VALID_COURSES)}")
    while True:
      try:
        marks=int(input("enter your marks in beetween 0 to 100"))
        if 0<=marks<=100:
          break
        else:
          print("marks must be in beetween 0 to 100")
      except ValueError:
        print("invalid input please enter a number") # if user enters any string or special character the exception will be handeled
    new_student={"id":student_id,
                  "name":name,
                  "course":course,
                  "marks":marks}
    students.append(new_student)
    print("student added successfully")
    from student_management_system.modules.export_data import export_students_to_csv
    export_students_to_csv() # to save the data after adding
    print("✅ Success: Student added successfully!")
