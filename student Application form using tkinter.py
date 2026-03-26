# Tkinter is Python’s built-in library for creating graphical user interfaces (GUIs).
# It supports layout management, event handling and customization, making it ideal for rapid GUI development in Python.

import tkinter as tk
import json
from datetime import datetime

root = tk.Tk()
root.title("Student Details Form")        #Title of the GUI interface

def submit_details():                     #Acceptance of all the user input in the form of Dictionary
    student_data = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "phone": phone_entry.get(),
        "favorite_language": lb.get(lb.curselection() if lb.curselection() else 0),
        "submission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        with open("student_details.json", "a") as f:             #creation of the json file named Student_details.json 
            json.dump(student_data, f, indent=4)
            f.write(",\n")
        status_label.config(text="Details saved successfully!")  #display at the end for success
        clear_fields()
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def clear_fields():                     #after submission re factor all to vacancies to add the next student details
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    lb.selection_clear(0, tk.END)

# Add input fields
tk.Label(root, text="Name:").pack()          #Root is the master here
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()         #Entering the Email ID
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Favorite Language:").pack()
lb = tk.Listbox(root)
lb.insert(0, "Python", "Java", "JavaScript", "C++")   #used in selecting an options from the tuple as their indexes and the preferences are all fixed.
lb.pack()

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_details)     #A button that after triggering will reset all the values and stores data
submit_btn.pack()                                                       #the data stored here is in the format of json file

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()                        #End of the GUI interface and the Master name here is : root
