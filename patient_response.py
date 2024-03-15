import tkinter as tk
from pymongo import MongoClient

# Create a new window
root = tk.Tk()

# Create a MongoDB client and connect to the database
client = MongoClient('mongodb://localhost:27017/')
db = client['Test_1']
table = db['Users_1']

# Set the window title and size
root.title("HealthyMe_Patient Response Page")
root.geometry("700x600")
root.resizable(False,False)

# Set the background color of the root window
root.configure(background="#f5e1df")

# Create a label for the patient name
name_label = tk.Label(root, text="PATIENT FULL NAME:")
name_label.pack(padx=13, pady=13)

# Create an entry field for the patient name
name_entry = tk.Entry(root, width=50)
name_entry.pack()

# Create a label for the first response question
question1_label = tk.Label(root, text="HOW ARE YOU FEELING TODAY?")
question1_label.pack(padx=13, pady=13)

# Create a text box for the patient's first response
response1_box = tk.Text(root, height=5)
response1_box.pack()

# Create a label for the second response question
question2_label = tk.Label(root, text="DID YOU TAKE YOUR MEDICATIONS ON TIME?")
question2_label.pack(padx=13, pady=13)

# Create a text box for the patient's second response
response2_box = tk.Text(root, height=5)
response2_box.pack()

# Create a label for the third response question
question3_label = tk.Label(root, text="HAVE YOU EXPERIENCED ANY SIDE EFFECTS FROM THE MEDICATIONS?")
question3_label.pack(padx=13, pady=13)

# Create a text box for the patient's third response
response3_box = tk.Text(root, height=5)
response3_box.pack()


def response():
    # Get user details from the entry boxes
    name = name_entry.get()
    response1 = response1_box.get("1.0", "end-1c")
    response2 = response2_box.get("1.0", "end-1c")
    response3 = response3_box.get("1.0", "end-1c")

    #db connection
    #Insert new user into MongoDB database
    new_user = {
        'Patient Name' : name,
        'Response 1' : response1,
        'Response 2' : response2,
        'Response 3' : response3,
        }

    result = table.insert_one(new_user)

# Create a button to submit the responses
submit_button = tk.Button(root, width=25, text="SUBMIT", fg="red", command=response)
submit_button.pack(padx=13, pady=13)
# Run the window
root.mainloop()
