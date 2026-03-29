import time
import calendar 
def month_calender(mm,yy):
    print("\n" + calendar.month(yy,mm))
    
def year_calender(yy):
    print("\n" + calendar.calendar(yy))

def is_leap_year(yy):
    return calendar.isleap(yy)

while True:
    print("**********************************")
    print("      Welcome to the calendar     ")
    print("**********************************")
    
    print('''\n''' + "1.Display the month in the calendar")
    print("2.Display the year in the calendar")
    print("3.To check whether the year is leap year or not")
    print("4.To Exit the Program")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))

        month_calender(mm,yy)

    elif choice == 2:
        yy = int(input("Enter year: "))
       
        year_calender(yy)
        
    elif choice == 3:
        yy = int(input("Enter year: "))
        if is_leap_year(yy):
            print(f"{yy} is a leap year.")
            break
        else:
            print(f"{yy} is not a leap year.")
            break
    
    elif choice == 4:
        print("Exiting the program...")
        time.sleep(2)
        break
    
    else:    
        print("Invalid choice!! Please Enter a valid choice")