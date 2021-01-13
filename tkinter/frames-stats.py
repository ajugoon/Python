
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Games Scheduler")
root.minsize(300, 300)
root.geometry("1000x700")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
planner = ttk.Notebook(root, width=1000, height=650)

# Create the frames of different colours that are 200*200 pixels in dimensions

tab1 = tk.Frame(planner, bg='lime green', width=300, height=300)
tab2 = tk.Frame(planner, bg='navy blue', width=300, height=300)

# Add the tabs/frames to the notebook object called "planner" 

planner.add(tab1, text='Home')
planner.add(tab2, text='Schedule')


# Needed for the Seahawks pic
Seahawks_logo = Image.open("Seahawks_logo.jpeg")
Seahawks_logo = Seahawks_logo.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
tkimage1 = ImageTk.PhotoImage(Seahawks_logo)

# Needed for the Partiots pic
Patriots_logo = Image.open("Patriots_logo.jpeg")
Patriots_logo = Patriots_logo.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
tkimage2 = ImageTk.PhotoImage(Patriots_logo)



def b1command():

	print ("executing b1 command")
	mycanvas1.create_image(20, 20, anchor='nw', image=tkimage1)

def b2command():

	print ("executing b2 command")
	mycanvas2.create_image(20, 20, anchor='nw', image=tkimage2)


Seahawks_b1 = tk.Button(tab1, text = "Welcome to the Seahawks schedule", height = 5, width = 25, command = b1command)
Patriots_b2 = tk.Button(tab2, text = "Welcome to the Patriots schedule", height = 5, width = 25, command = b2command)

mycanvas1 = tk.Canvas(tab1, bg="blue", height=400, width=300)
mycanvas2 = tk.Canvas(tab2, bg="blue", height=400, width=300)


planner.grid(row = 0, column = 0)

Seahawks_b1.grid(row=0, column=2)
Patriots_b2.grid(row=0, column=2)

mycanvas1.grid(row=0, column=4)
mycanvas2.grid(row=0, column=4)

root.mainloop()

