# Example 6: Message Boxes

import tkinter as tk
from tkinter import messagebox

def submit():
    if entry.get() == "":
        messagebox.showerror("Error", "Input cannot be empty")
    else:
        messagebox.showinfo("Success", "Submission received")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Submit", command=submit).pack()

root.mainloop()

