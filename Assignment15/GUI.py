import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.title("Age Calculator")
window.geometry("300x200")  # Set window size

# Create a form for data entry
form = tk.Frame(window)
form.pack()

# Create a text box for name input
name_label = tk.Label(form, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(form)
name_entry.grid(row=0, column=1)

# Create a text box for age input
age_label = tk.Label(form, text="Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(form)
age_entry.grid(row=1, column=1)

# Create a button to submit the form
def submit_data():
    # Get the name and age from the text boxes
    name = name_entry.get()
    age_str = age_entry.get()

    # Check if age is a valid number
    try:
        age = int(age_str)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for age.")
        return

    # Calculate the age in 5 years
    future_age = age + 5

    # Display the result
    result_label = tk.Label(window, text=f"In 5 years, {name} will be {future_age} years old.")
    result_label.pack()

submit_button = tk.Button(window, text="Submit", command=submit_data)
submit_button.pack()

window.mainloop()