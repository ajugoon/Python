# tk introductory example 
# showing the use of the "pack" layout manager

import tkinter as tk
root = tk.Tk() # root is the name of the GUI object
root.title("My TKinter Program") 
root.minsize(300, 300) # height and width in pixels
root.geometry ("300x500")


b1 = tk.Button(root, text="One", height = 10, width = 10) # set in "units of text"
b2 = tk.Button(root, text="Two", height = 10, width = 10) # set in "units of text"
b3 = tk.Button(root, text = "Three", height = 10, width = 10) # set in "units of text"

b1.pack(side=tk.BOTTOM)
b2.pack(side=tk.BOTTOM)
b3.pack(side=tk.BOTTOM)

root.mainloop()