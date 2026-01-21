# Example 4: Layout with Frames and "Grid"
# NOTE: Do not mix pack() and grid() in the same container

import tkinter as tk

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Username").grid(row=0, column=0)
tk.Entry(frame).grid(row=0, column=1)

tk.Label(frame, text="Password").grid(row=1, column=0)
tk.Entry(frame, show="*").grid(row=1, column=1)

root.mainloop()


