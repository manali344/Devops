"""2 Student Grades
Create a dictionary where the keys are student names and the values are their grades. Allow the user to:
Add a new student and grade.
Update an existing student’s grade.
Print all student grades.
"""




student_details = {
    "Akash" : "A",
    "Shruti": "B"
}

def add(student_name,student_grade):
    student_details[student_name] = student_grade
    print(student_details)

def display_det():
    return student_details

def update(stud_name,new_grade):
    if stud_name in student_details:    
        try:
            student_details[stud_name] = new_grade
            return 0
        except:
            return 2
    else:
        return 1

while True:
    print("Choose any option from below :\n")
    print("1: Add student details")
    print("2: Update student details")
    print("3: All student details")
    choice = int(input())  
    if choice == 1:
        student_name = input("Please enter name of Student: ")
        student_grade = input("Please enter grade of Student: ")
        add(student_name,student_grade)
        
    elif choice == 2:
        stud_name = input("Enter the name of student whose grade is to be updated: ")
        new_grade = input("Enter New Grade: ")
        ack = update(stud_name,new_grade)
        if ack == 0:
            print("Record successfully updated")
        elif ack == 1:
            print("Record not found")
        else:
            print("Issue in updating the record")
    elif choice == 3:
        result = display_det()
        print(result)
    else:
        print("Please choose correct option")
    print("Do you want to continue? (Yes/No)")
    cont = input()
    if cont.lower() == 'no':
        break