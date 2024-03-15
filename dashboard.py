import tkinter as tk
import subprocess

# Create a new window
root = tk.Tk()

# Set the window title and size
root.title("HealthyMe_Dashboard")
root.geometry("550x550")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#e7eafe")

# Define colors for the buttons
button_color = "#FFFFFF"   # white
text_color = "#000000"     # black

#Redirect  to Dashboard
def run_login():
    subprocess.Popen(['python', 'login.py'])

#Redirect  to Dashboard
def run_register():
    subprocess.Popen(['python', 'register.py'])

#Redirect  to Dashboard
def run_appointment():
    subprocess.Popen(['python', 'medicine_reminder.py'])

#Redirect  to Dashboard
def run_facts():
    subprocess.Popen(['python', 'facts.py'])

#Redirect  to Dashboard
def run_location():
    subprocess.Popen(['python', 'location.py'])

#Redirect  to Dashboard
def run_patient_preferences():
    subprocess.Popen(['python', 'patient_preferences.py'])

#Redirect  to Dashboard
def run_patient_responses():
    subprocess.Popen(['python', 'patient_response.py'])

#Redirect  to Dashboard
def run_timer():
    subprocess.Popen(['python', 'appointment.py'])
    
# Creating buttons
login_button = tk.Button(root, text="LOGIN", bg=button_color, fg="green", font="Arial", bd=2, width=32, height=2, command=run_login)
login_button.pack(pady=5)

register_button = tk.Button(root, text="REGISTER", bg=button_color, fg="brown", font="Arial", bd=2, width=32, height=2, command=run_register)
register_button.pack(pady=10)

button1 = tk.Button(root, text="MEDICINE REMINDER", bg=button_color, fg="blue", font="Arial", bd=2, width=32, height=2, command=run_appointment)
button1.pack(pady=10)

button2 = tk.Button(root, text="FACTS", bg=button_color, fg="red", font="Arial", bd=2, width=32, height=2, command=run_facts)
button2.pack(pady=10)

button3 = tk.Button(root, text="LOCATION", bg=button_color, fg="purple", font="Arial", bd=2, width=32, height=2, command=run_location)
button3.pack(pady=10)

button4 = tk.Button(root, text="PATIENT PREFERENCES", bg=button_color, fg="blue", font="Arial", bd=2, width=32, height=2, command=run_patient_preferences)
button4.pack(pady=10)

button5 = tk.Button(root, text="PATIENT RESPONSES", bg=button_color, fg="red", font="Arial", bd=2, width=32, height=2, command=run_patient_responses)
button5.pack(pady=10)

button6 = tk.Button(root, text="APPOINTMENT", bg=button_color, fg="purple", font="Arial", bd=2, width=32, height=2, command=run_timer)
button6.pack(pady=10)

# Run the window
root.mainloop()
