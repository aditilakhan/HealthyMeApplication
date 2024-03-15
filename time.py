import tkinter as tk
import time

# Create a new window
root = tk.Tk()

# Set the window title and size
root.title("HealthyMe_Digital Clock")
root.geometry("330x200")
root.resizable(False,False)

# Create a label for the time
time_label = tk.Label(root, font=("Arial", 30, "bold"), bg="light blue", fg="white")
time_label.pack(fill=tk.BOTH, expand=True)

# Define a function to update the time label
def update_time():
    current_time = time.strftime("%H:%M:%S")
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

# Call the update_time() function once to start the clock
update_time()

# Run the window
root.mainloop()
