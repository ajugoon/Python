# tk introductory example 

import tkinter as tk
root = tk.Tk() # root is the name of the GUI object
root.title("My TKinter Program") 
root.minsize(300, 300) # height and width in pixels
root.geometry ("400x300")


b1 = tk.Button(root, text="One")
b2 = tk.Button(root, text="Two")
b1.pack(side=tk.LEFT)
b2.pack(side=tk.LEFT)

root.mainloop()