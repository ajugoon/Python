# Example 3: User Input with Entry Widgets

import tkinter as tk

def greet():
    name = entry.get()
    label.config(text=f"Hello, {name}!")

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Greet Me", command=greet)
button.pack()

label = tk.Label(root, text="")
label.pack()

root.mainloop()

