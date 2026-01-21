# Example 2: Labels, Buttons, and Packing Widgets

import tkinter as tk

def say_hello():
    label.config(text="Hello, world!")

root = tk.Tk()

label = tk.Label(root, text="Click the button")
label.pack()

button = tk.Button(root, text="Say Hello", command=say_hello)
button.pack()

root.mainloop()

