import subprocess
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.title("HealthyMe_Welcome")
root.geometry("780x650")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#e7eafe")

label1 = tk.Label(root, text="HEALTHY ME : HEALTH REMINDER APPLICATION", font=('Arial', 20, 'bold'))
label1.pack(padx=20,pady=20)

# Open the image file and resize it
image_file = "app_welcome_screen.png"
image = Image.open(image_file)
resized_image = image.resize((650,380), Image.ANTIALIAS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label widget to display the image
background_label = tk.Label(root, image=photo)
background_label.pack(fill=tk.BOTH, expand=True)

#Redirect  to Dashboard
def run_dashboard():
    subprocess.Popen(['python', 'dashboard.py'])
    
# Create the dashboard button 
button1 = tk.Button(root, text="GO TO DASHBOARD", bg="white", fg="black", width=70, height=5, font = "Palatino", relief="groove", bd=5, command=run_dashboard)
button1.pack(side=tk.BOTTOM, padx = 20, pady=20)

root.mainloop()
