# Tkinter is Python’s built-in library for creating graphical user interfaces (GUIs).
# It supports layout management, event handling and customization, making it ideal for rapid GUI development in Python.




import tkinter as tk
import json
from datetime import datetime

root = tk.Tk()
root.title("Student Details Form")

def submit_details():
    student_data = {
        "name": name_entry.get(),
        "email": email_entry.get(),
        "phone": phone_entry.get(),
        "favorite_language": lb.get(lb.curselection() if lb.curselection() else 0),
        "submission_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    try:
        with open("student_details.json", "a") as f:
            json.dump(student_data, f, indent=4)
            f.write(",\n")
        status_label.config(text="Details saved successfully!")
        clear_fields()
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}")

def clear_fields():
    name_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    lb.selection_clear(0, tk.END)

# Add input fields
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email:").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone:").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Favorite Language:").pack()
lb = tk.Listbox(root)
lb.insert(0, "Python", "Java", "JavaScript", "C++")
lb.pack()

# Submit button
submit_btn = tk.Button(root, text="Submit", command=submit_details)
submit_btn.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
