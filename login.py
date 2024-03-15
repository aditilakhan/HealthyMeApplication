import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
table = db['Users_1']

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title("HealthyMe_Login")
        self.root.geometry("400x380")
        root.resizable(False,False)

        # Set the background color of the root window
        root.configure(background="#e1f2db")
        
        # Create labels and entry boxes for login details
        tk.Label(root, text="USERNAME:").grid(row=0, column=0, padx=10, pady=10)
        self.username_entry = tk.Entry(root, width=40)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="PASSWORD:").grid(row=1, column=0, padx=10, pady=10)
        self.password_entry = tk.Entry(root, show="*", width=40)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
 
        
        # Create a button to submit the login details
        tk.Button(root, width=20, text="LOGIN", fg="green", command=self.login).grid(row=2, column=1)


    def login(self):
        # Get login details from the entry boxes
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if username and password are correct
        user = table.find_one({'username': username, 'password': password})
        if user:
            messagebox.showinfo("Success", "Login successful")
        else:
            messagebox.showinfo("Error", "Incorrect username or password")

        #Redirect  to Medicine Reminder
        def run_login():
            subprocess.Popen(['python', 'medicine_reminder.py'])
            
root = tk.Tk()
login_page = LoginPage(root)
root.mainloop()
