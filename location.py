import tkinter as tk
import webbrowser
from PIL import Image, ImageTk
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['Test_1']
users = db['Users_1']

def search_location():
    location = location_entry.get()
    url = "https://www.google.com/maps/search/?api=1&query=" + location
    webbrowser.open_new_tab(url)
    #db insert
    users.insert_one({"location":location})

root = tk.Tk()
root.geometry("450x450")
root.title("HealthyMe_Nearby search")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#eae1ff")

# Location label and entry widget
location_label = tk.Label(root, text="ENTER LOCATION: ")
location_label.pack(pady=10)
location_entry = tk.Entry(root, width=50)
location_entry.pack(pady=5)

# Search button
search_button = tk.Button(root, width=30, text="SEARCH", fg="purple", command=search_location)
search_button.pack(pady=10)

# Open the image file and resize it
image_file = "map.png"
image = Image.open(image_file)
resized_image = image.resize((300,300), Image.ANTIALIAS)

# Create a PhotoImage object from the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label widget to display the image
background_label = tk.Label(root, image=photo)
background_label.pack(fill=tk.BOTH, expand=True)

root.mainloop()
