import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
from pymongo import MongoClient

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
table = db['Users_1']

# Create a new window
root = tk.Tk()

# Set the window title and size
root.title("HealthyMe_AppointmentScheduling")
root.geometry("550x300")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#eae1ff")

# Create labels and entry widgets for patient information
name_label = tk.Label(root, text="PATIENT FULL NAME:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

contact_label = tk.Label(root, text="CONTACT NO:")
contact_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

contact_entry = tk.Entry(root)
contact_entry.grid(row=1, column=1, padx=5, pady=5)

email_label = tk.Label(root, text="E-MAIL ADDRESS:")
email_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

# Create a label for selecting appointment date
date_label = tk.Label(root, text="APPOINTMENT DATE (YYYY-MM-DD):")
date_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

date_entry = tk.Entry(root)
date_entry.grid(row=3, column=1, padx=5, pady=5)

# Create a drop-down menu for selecting appointment time
time_label = tk.Label(root, text="APPOINTMENT TIME:")
time_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

time_options = ["9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM"]
time_var = tk.StringVar(root)
time_var.set(time_options[0])
time_menu = tk.OptionMenu(root, time_var, *time_options)
time_menu.grid(row=4, column=1, padx=5, pady=5)

# Create a button to submit the form
submit_button = tk.Button(root, width=25, text="SCHEDULE AN APPOINTMENT!", fg="purple", command=lambda: save_appointment())
submit_button.grid(row=5, column=1, padx=5, pady=10, sticky="e")

# Function to save the appointment
def save_appointment():
    name = name_entry.get()
    contact = contact_entry.get()
    email = email_entry.get()
    date = date_entry.get()
    time = time_var.get()

    # Check if appointment date is in the future
    now = datetime.now()
    appointment_datetime = datetime.strptime(date + " " + time, "%Y-%m-%d %I:%M %p")
    if appointment_datetime < now:
        messagebox.showerror("Error", "Appointment date and time must be in the future.")
        return

    # Save appointment to database or file
    #Insert new user into MongoDB database
    new_user = {
        'name' : name,
        'contact' : contact,
        'email' : email,
        'date' : date,
        'time' : time,
        }

    result = table.insert_one(new_user)
    if result.inserted_id:
        messagebox.showinfo("Database insertion successful")
    else:
        messagebox.showinfo("Failed to insert user into database")

    # Show success message
    messagebox.showinfo("Success", "Appointment scheduled.")

# Run the window
root.mainloop()
