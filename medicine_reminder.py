from tkinter import *
import datetime
from tkinter import messagebox
from pymongo import MongoClient

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
users = db['Users_2']

class MedicineReminder:
    def __init__(self, master):
        self.master = master
        self.master.title("HealthyMe_MedicineReminder")
        self.master.geometry("500x460")
        root.resizable(False,False)

        # Set the background color of the root window
        root.configure(background="#e6f3f5")

        # Create the labels
        self.label1 = Label(master, text="ADD A MEDICINE:")
        self.label2 = Label(master, text="DOSAGE:")
        self.label3 = Label(master, text="SET TIME:")
        self.label4 = Label(master, text="ADD A NOTE:")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        self.label2.grid(row=1, column=0, padx=10, pady=10)
        self.label3.grid(row=2, column=0, padx=10, pady=10)
        self.label4.grid(row=3, column=1, padx=10, pady=10)
        
        # Create the entry fields
        self.med_name = Entry(master, width=30)
        self.dosage = Entry(master, width=30)
        self.time = Entry(master, width=30)
        self.notes = Text(master, width=30, height=5)
        self.med_name.grid(row=0, column=1, padx=10, pady=10)
        self.dosage.grid(row=1, column=1, padx=10, pady=10)
        self.time.grid(row=2, column=1, padx=10, pady=10)
        self.notes.grid(row=3, column=1, padx=10, pady=10)
        
        # Create the submit button
        self.submit_button = Button(master, text="ADD A REMINDER!", fg="blue", command=self.add_reminder)
        self.submit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Create the reminder list
        self.reminder_list = Listbox(master, width=50)
        self.reminder_list.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
    def add_reminder(self):
        # Get the values from the entry fields
        med_name = self.med_name.get()
        dosage = self.dosage.get()
        time = self.time.get()
        notes = self.notes.get("1.0", END).strip()
        
        # Check if all fields are filled out
        if med_name == "" or dosage == "" or time == "":
            messagebox.showwarning("Warning", "Please fill out all fields")
        else:
            # Add the reminder to the listbox
            reminder = f"{med_name} - {dosage} - {time} - {notes}"
            self.reminder_list.insert(END, reminder)

        #db connection
        #Insert new user into MongoDB database
        new_user = {
            'add a medicine': med_name,
            'dosage' : dosage,
            'set time' : time,
            'add a note' : notes,
            }
        result = users.insert_one(new_user)
        
        # Clear the entry fields
        self.med_name.delete(0, END)
        self.dosage.delete(0, END)
        self.time.delete(0, END)
        self.notes.delete("1.0", END)
            
        # Schedule the reminder
        self.schedule_reminder(time, med_name, dosage, notes)
            
    def schedule_reminder(self, time, med_name, dosage, notes):
        now = datetime.datetime.now()
        reminder_time = datetime.datetime.strptime(time, "%H:%M")
        if reminder_time < now.time():
            reminder_time += datetime.timedelta(days=1)
        delta = reminder_time - now.time()
        seconds = delta.seconds
        
        # Use tkinter's after method to schedule the reminder
        self.master.after(seconds * 1000, self.show_reminder, reminder)
        
    def show_reminder(self, reminder):
        messagebox.showinfo("Reminder", reminder)
        
root = Tk()
app = MedicineReminder(root)
root.mainloop()
        
        
