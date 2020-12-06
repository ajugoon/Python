# Tkinter introductory example 
# Showing the use of the "grid" layout manager
# Enabling buttons to work 
# Introducing the "FRAME" for Images
# Adding in JPEGS.
# Reference: https://stackoverflow.com/questions/54716337/tkinter-how-to-place-image-into-a-frame
# Reference: https://www.reddit.com/r/learnpython/comments/axscem/tkinter_resize_an_image_before_putting_it_on/

import tkinter as tk
from PIL import ImageTk, Image # we need PILLOW to display images

root = tk.Tk() # root is the name of the GUI object
root.title("My TKinter Program") 
root.minsize(300, 300) # height and width in pixels
root.geometry ("600x500")

# Set up your variables
myBGColour = "yellow"

# Set up your images
img = Image.open("hydrogen.jpeg")
img = img.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
tkimage1 = ImageTk.PhotoImage(img)

###

# Define all of your functions to be used later in the program

def b1command():
	print ("executing b1 command")
	#mycanvas.image = ImageTk.PhotoImage(tkimage1.resize((200, 200), Image.ANTIALIAS))
	mycanvas.create_image(20, 20, anchor='nw', image=tkimage1)
	

def b2command():
	print ("executing b2 command")
	

def b3command():
	print ("executing b3 command")
	

def b4command():
	print ("executing b4 command")
	

def b5command():
	print ("executing b5 command")
	

def b6command():
	print ("executing b6 command")


# Create your buttons
# Note the height and the width are set in "units of text"
b1 = tk.Button(root, text = "Red", height = 10, width = 10, command = b1command) 
b2 = tk.Button(root, text = "Orange", height = 10, width = 10, command = b2command) 
b3 = tk.Button(root, text = "Yellow", height = 10, width = 10, command = b3command) 
b4 = tk.Button(root, text = "Blue", height = 10, width = 10, command = b4command) 
b5 = tk.Button(root, text = "Green", height = 10, width = 10, command = b5command) 
b6 = tk.Button(root, text = "Violet", height = 10, width = 10, command = b6command) 

# Create your canvas/frame as needed into which the image will be placed

mycanvas = tk.Canvas(root, bg="blue", height=400, width=300)

# Position everything using the Grid Layout Manager

# Along Row 0
b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

# Along Row 1
b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

# Frame is placed in Column 3, Row 0 and will span 2 rows downward

mycanvas.grid(row=0, column=3, rowspan=2)

root.mainloop()
