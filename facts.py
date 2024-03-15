import tkinter as tk
import random
from pymongo import MongoClient
from PIL import Image, ImageTk

# Connect to MongoDB database
#connection to mongodb
client = MongoClient('mongodb://localhost:27017')
#connection to specified database
db = client['Test_1']
#connection to specified table
users = db['Users_1']

# Create a new window
root = tk.Tk()

# Set the window title and size
root.title("HealthyMe_Health Facts")
root.geometry("680x500")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#f5e1df")


# Create a list of health facts
health_facts = [
    "Fact  : Drinking water can help you lose weight",
    "Fact  : Eating a balanced diet can improve your mental health",
    "Fact  : Getting enough sleep can increase focus and productivity",
    "Fact  : Make sure you do lots of sports and stay active",
    "Fact  : Regular exercise can reduce your risk of chronic diseases",
    "Fact  : Stress can have negative effects on your physical and mental health",
    "Fact  : Studies have shown that laughter can really benefit your health and mood", 
    "Fact  : Staying hydrated boosts your metabolism",
    "Fact  : It is important to prioritize self-care and take time for relaxation",
    "Fact  : Washing your hands regularly can help prevent the spread of germs and infections",
    "Fact  : Regular check-ups with a healthcare provider can help detect and treat health problems early",
    "Fact  : Adequate hydration is important for maintaining healthy bodily functions",
    "Fact  : Fruits and vegetables are important sources of vitamins, minerals, and fiber",
    "Fact  : Regular physical activity can improve brain function",
    "Fact  : Sitting for prolonged periods can increase the risk of chronic disease",
    "Fact  : Eating a diet rich in plant-based foods can reduce the risk of chronic diseases",
    "Fact  : Regular meditation and mindfulness practices can reduce stress and improve mental health",
    "Fact  : A healthy diet can improve energy levels and overall well-being",
    
]

# Define a function to display a random fact
def display_fact():
    # Select a random fact from the list
    fact = random.choice(health_facts)
    #db insert
    users.insert_one({"Facts":fact})

    # Update the fact label text
    fact_label.config(text=fact)

# Open the image file and resize it
image_file = "fact_img.png"
image = Image.open(image_file)
resized_image = image.resize((350,300), Image.ANTIALIAS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label widget to display the image
background_label = tk.Label(root, image=photo)
background_label.pack(fill=tk.BOTH, expand=True)

# Create a label for the page title
title_label = tk.Label(root, width=30, text="HEALTH FACTS", fg="blue", font=("Arial", 15))
title_label.pack(pady=10)

# Create a label for the fact
fact_label = tk.Label(root, text="", font=("Arial", 12))
fact_label.pack(pady=5)

# Create a button to display a new fact
fact_button = tk.Button(root, width=30, text="CLICK ON TO NEW FACTS >", fg="RED", command=display_fact)
fact_button.pack(pady=10)


# Run the window
root.mainloop()
