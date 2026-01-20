# Example 5: Control Flow & State (Checkboxes and Radio Buttons)

import tkinter as tk

def show_choice():
    label.config(text=f"You chose: {choice.get()}")

root = tk.Tk()

choice = tk.StringVar(value="None")

tk.Radiobutton(root, text="Option A", variable=choice, value="A").pack()
tk.Radiobutton(root, text="Option B", variable=choice, value="B").pack()

tk.Button(root, text="Confirm", command=show_choice).pack()
label = tk.Label(root, text="")
label.pack()

root.mainloop()


