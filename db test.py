from tkinter import *
import pymongo

# connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Test_1"]
collection = db["Users_1"]

# define function to insert data into MongoDB
def insert_data():
    data = textbox.get("1.0", "end-1c")
    collection.insert_one({"data": data})

# create GUI window
window = Tk()
window.title("Data Input Form")

# create textbox widget
textbox = Text(window, height=10, width=50)
textbox.pack()

# create button widget
button = Button(window, text="Submit", command=insert_data)
button.pack()

# start the GUI event loop
window.mainloop()
