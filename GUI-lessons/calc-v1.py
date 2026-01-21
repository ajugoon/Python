# Example: A very simple addition calculator.

import tkinter as tk

def add_numbers():
    num1 = entry1.get()
    num2 = entry2.get()

    if num1.isdigit() and num2.isdigit():
        result = int(num1) + int(num2)
        result_label.config(text=f"Result: {result}")
    else:
        result_label.config(text="Please enter valid numbers")

# Create the main window
root = tk.Tk()
root.title("Add Two Numbers")

# First number
tk.Label(root, text="First Number:").pack()
entry1 = tk.Entry(root)
entry1.pack()

# Second number
tk.Label(root, text="Second Number:").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Add button
tk.Button(root, text="Add", command=add_numbers).pack()

# Result label
result_label = tk.Label(root, text="Result:")
result_label.pack()

# Start the program
root.mainloop()


