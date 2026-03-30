import time

print("press [ENTER] to start the stop watch")
input()   ##Checks for only the Enter key pressed, and ignores any other input
starting_time = time.perf_counter()  #Performance Counter

print("******************************")
print("      STOP WATCH STARTED      ")
print("******************************")

print("press [ENTER] to stop the stop watch")
input()   #Checks for only the Enter key pressed, and ignores any other input
ending_time = time.perf_counter()

print("******************************")
print("      STOP WATCH STOPPED      ")
print("******************************")

Elapsed_time = ending_time - starting_time   #The time diffrence between the first Enter and the second Enter pressed

hours = Elapsed_time // 3600   #1 Hour = 3600 Seconds   this keeps the whole number part of the division, which represents the number of hours in the elapsed time. 
                               # The remaining seconds after calculating hours is used to calculate minutes and seconds.
minutes = (Elapsed_time % 3600) // 60  #after calculating hours, the remaining seconds are calculated using the modulus operator (%),
                                       # and then divided by 60 to get the number of minutes in the elapsed time.

seconds = Elapsed_time % 60 #The remaining seconds after calculating hours and minutes is used to calculate seconds

milliseconds = (Elapsed_time - int(Elapsed_time)) * 1000

print(f"Elapsed time: {int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds, {int(milliseconds)} milliseconds")


