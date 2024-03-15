import subprocess
import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
table = db['Users_1']

class RegistrationPage:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthyMe_Register")
        self.root.geometry("500x510")
        root.resizable(False,False)

        # Set the background color of the root window
        root.configure(background="#f5e8da")

        # Create labels and entry boxes for user details
        tk.Label(root, text="FIRST NAME:").grid(row=0, column=0)
        self.first_name_entry = tk.Entry(root, width=50)
        self.first_name_entry.grid(row=0, column=1, padx=15, pady=15)

        tk.Label(root, text="LAST NAME:").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(root, width=50)
        self.last_name_entry.grid(row=1, column=1, padx=15, pady=15)

        tk.Label(root, text="GENDER:").grid(row=2, column=0)
        self.gender_entry = tk.StringVar(root)
        self.gender_entry.set("Male")
        gender_options = ["Male", "Female", "Other"]
        tk.OptionMenu(root, self.gender_entry, *gender_options).grid(row=2, column=1, padx=15, pady=15)

        tk.Label(root, text="AGE:").grid(row=3, column=0)
        self.age_entry = tk.Entry(root, width=50)
        self.age_entry.grid(row=3, column=1, padx=15, pady=15)

        tk.Label(root, text="CONTACT NO:").grid(row=4, column=0)
        self.contact_number_entry = tk.Entry(root, width=50)
        self.contact_number_entry.grid(row=4, column=1, padx=15, pady=15)

        tk.Label(root, text="E-MAIL ADDRESS:").grid(row=5, column=0)
        self.email_entry = tk.Entry(root, width=50)
        self.email_entry.grid(row=5, column=1, padx=15, pady=15)

        tk.Label(root, text="USERNAME:").grid(row=6, column=0)
        self.username_entry = tk.Entry(root, width=50)
        self.username_entry.grid(row=6, column=1, padx=15, pady=15)

        tk.Label(root, text="PASSWORD:").grid(row=7, column=0)
        self.password_entry = tk.Entry(root, show="*", width=50)
        self.password_entry.grid(row=7, column=1, padx=15, pady=15)

        tk.Label(root, text="CONFIRM PASSWORD:").grid(row=8, column=0)
        self.confirm_password_entry = tk.Entry(root, show="*", width=50)
        self.confirm_password_entry.grid(row=8, column=1, padx=15, pady=15)

        # Create a button to submit the form
        tk.Button(root, width=30, text="REGISTERED", fg="red", command=self.register).grid(row=9, column=1, padx=15, pady=15)

    def register(self):
        # Get user details from the entry boxes
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_entry.get()
        age = self.age_entry.get()
        contact_number = self.contact_number_entry.get()
        email = self.email_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Validate user details
        if not first_name:
            messagebox.showerror("Error", "Please enter all credentials!")
            return

        if not last_name:
            messagebox.showerror("Error", "Please enter your last name")
            return

        if not age:
            messagebox.showerror("Error", "Please enter your age")
            return

        if not contact_number:
            messagebox.showerror("Error", "Please enter your contact number")
            return

        if not email:
            messagebox.showerror("Error", "Please enter your email address")
            return
        

        #db connection
        #Insert new user into MongoDB database
        new_user = {
            'first_name' : first_name,
            'last_name' : last_name,
            'gender' : gender,
            'age' : age,
            'contact_number' : contact_number,
            'email' : email,
            'username' : username,
            'password' : password,
            'confirm_password' : confirm_password,
            }

        # Create error and success labels
        error_label = tk.Label(root, fg="red").grid(row=10, column=1)

        success_label = tk.Label(root, fg="green").grid(row=11, column=1)
        
        result = table.insert_one(new_user)
        if result.inserted_id:
            messagebox.showinfo("Database insertion successful")
        else:
            messagebox.showinfo("Failed to insert user into database")

        # Show a success message
        messagebox.showinfo("Success", "Registration Successful")

root = tk.Tk()
registration_page = RegistrationPage(root)
root.mainloop()

#Redirect  to Dashboard
def run_dashboard():
    subprocess.Popen(['python', 'dashboard.py'])
