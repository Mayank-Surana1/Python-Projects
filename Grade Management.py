#Managing student grades is a fundamental task in any educational setting, from a single classroom to an entire institution.
#with its intuitive syntax and powerful data structures
#it offers an excellent platform for developing efficient grade management systems. 
# This article will dive deep into leveraging Python dictionaries to create a comprehensive and flexible system for tracking student performance.



def grades(stud,marks):      #Used to Display Grades and to hand;e the exceptions
    if marks >= 90:
        print(f"{stud:<10}  A ")
    elif marks >= 80 and marks < 90:
        print(f"{stud:<10}  B ")
    elif marks >= 70 and marks < 80:
        print(f"{stud:<10}  C ")
    elif marks >= 50 and marks < 70:
        print(f"{stud:<10}  D ")
    elif marks < 50:
        print(f"{stud:<10}  F ")
    else:
        try:
            print(f"{stud:<10}  NULL")
        except AttributeError:
            print("Invalid input for marks. Please enter a valid number.")
arr = {}    #A dict to store the key value pairs of the student details
no_of_students = int(input("Enter the number of students: "))
for i in range(no_of_students):
    name = input("Enter the name of the student: ")    #Details of the n student gets input by the user via loop
    mark = int(input("Enter the marks of the student: "))
    arr[name] = mark

print("*" * 20)    #These are the decorators
print("\nGrade Report")
print("Name       Grade")
for name, mark in arr.items():
        grades(name, mark)
print("*" * 20)

