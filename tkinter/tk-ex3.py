# tk introductory example 
# showing the use of the "grid" layout manager

import tkinter as tk
root = tk.Tk() # root is the name of the GUI object
root.title("My TKinter Program") 
root.minsize(300, 300) # height and width in pixels
root.geometry ("300x500")

# Note the height and the width are set in "units of text"
b1 = tk.Button(root, text = "One", height = 10, width = 10) 
b2 = tk.Button(root, text = "Two", height = 10, width = 10) 
b3 = tk.Button(root, text = "Three", height = 10, width = 10) 
b4 = tk.Button(root, text = "Four", height = 10, width = 10) 
b5 = tk.Button(root, text = "Five", height = 10, width = 10) 
b6 = tk.Button(root, text = "Six", height = 10, width = 10) 

# Along Row 0
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

# Along Row 1
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

root.mainloop()