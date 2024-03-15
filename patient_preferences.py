import tkinter as tk
from tkinter import messagebox
import geocoder 
import requests
from pymongo import MongoClient

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
table = db['Users_1']

# Create a new window
root = tk.Tk()

# Set the window title and size
root.title("HealthyMe_Patient Preference")
root.geometry("600x400")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#e6f3f5")

# Create labels and entry widgets for patient information
name_label = tk.Label(root, text="PATIENT FULL NAME:")
name_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

name_entry = tk.Entry(root, width=50)
name_entry.grid(row=0, column=1, padx=5, pady=5)

address_label = tk.Label(root, text="PATIENT ADDRESS:")
address_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

address_entry = tk.Entry(root, width=50)
address_entry.grid(row=1, column=1, padx=5, pady=5)

# Create labels and option menus for hospital and location preference
hospital_label = tk.Label(root, text="PREFERRED ON NEARBY SEARCH HOSPITAL:")
hospital_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")

hospital_options = ["Hospital A", "Hospital B", "Hospital C"]
hospital_var = tk.StringVar(root)
hospital_var.set(hospital_options[0])
hospital_menu = tk.OptionMenu(root, hospital_var, *hospital_options)
hospital_menu.grid(row=2, column=1, padx=10, pady=10)

location_label = tk.Label(root, text="PREFERRED LOCATION:")
location_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")

location_options = ["Location A", "Location B", "Location C"]
location_var = tk.StringVar(root)
location_var.set(location_options[0])
location_menu = tk.OptionMenu(root, location_var, *location_options)
location_menu.grid(row=3, column=1, padx=10, pady=10)

# Create a button to submit the form
submit_button = tk.Button(root, width=20, text="SUBMIT", fg="blue", command=lambda: save_preferences())
submit_button.grid(row=5, column=0, padx=5, pady=5, sticky="e")

# Function to save patient preferences
def save_preferences():
    name = name_entry.get()
    address = address_entry.get()
    hospital = hospital_var.get()
    location = location_var.get()

    #Insert new user into MongoDB database
    new_user = {
        'Name' : name,
        'Address' : address,
        'Hospital' : hospital,
        'Location' : location,
        }
    result = table.insert_one(new_user)

    
"""
    # Use geocoder module to get latitude and longitude of patient address
    try:
        g = geocoder.osm(address)
        latitude, longitude = g.latlng
    except:
        messagebox.showerror("Error", "Could not get location from address.")
        return

    # Use requests module to get distance from patient address to preferred hospital
    try:
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins={latitude},{longitude}&destinations={hospital}&key=API_KEY_HERE"
        response = requests.get(url).json()
        distance = response["rows"][0]["elements"][0]["distance"]["text"]
    except:
        messagebox.showerror("Error", "Could not get distance to preferred hospital.")
        return
"""
    # Save patient preferences to database or file
    # ...
    
# Run the window
root.mainloop()
