def grades(stud,marks):
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
arr = {}
no_of_students = int(input("Enter the number of students: "))
for i in range(no_of_students):
    name = input("Enter the name of the student: ")
    mark = int(input("Enter the marks of the student: "))
    arr[name] = mark

print("*" * 20)
print("\nGrade Report")
print("Name       Grade")
for name, mark in arr.items():
        grades(name, mark)
print("*" * 20)

