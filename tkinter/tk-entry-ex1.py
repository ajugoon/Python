# A simple Entry Widget example

import tkinter as tk

#Creates a window of a particular size
root = tk.Tk()
root.title("Entry Widget example")
root.geometry('400x200')

# Helper function to add two numbers together
def getInfo():
    num1 = (number1.get())
    label2.config(text="The number entered was " + str(num1))
 
# Create your widgets
# The StringVar instance holds data from the Entry Widget
number1 = tk.StringVar()
entry1 = tk.Entry(root, textvariable=number1)


# a Label widget
label1 = tk.Label(root, text="Enter your number: ")

# another Label widget
label2 = tk.Label(root, 
    bg = "blue", 
    fg = "light green",
    font = "Helvetica 16 bold italic",
    text="Your number is: ")


# a Button widget
button1 = tk.Button(root, text="Get Number", command=getInfo)

# place all widgets into the "root" window using grid
label1.grid(row=0, column=0)
entry1.grid(row=1, column=0)
label2.grid(row=2, column=0)
button1.grid(row=3, column=0)


# main Loop
root.mainloop()
