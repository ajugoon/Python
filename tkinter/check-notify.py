
import tkinter as tk
from PIL import ImageTk,Image
import random
import time
from tkinter import messagebox
#import tkMessageBox

root = tk.Tk()
root.title("Medsmart") 
root.geometry("900x400")
      
var1 = tk.IntVar()
var2 = tk.IntVar()
var = tk.StringVar()
d = tk.StringVar()
options = ["yes", "no"]

def var_states():

    p1 = var1.get()
    p2 = var2.get()
    print("Pill 1: %d,\nPill 2: %d" % (p1, p2))

    if (p1 == 0 and p2 == 0):
        messagebox.showinfo("Notification", "Time to take Warfarin and Tylenol")
    elif (p1 == 0 and p2 == 1):
        messagebox.showinfo("Notification", "Time to take Warfarin")
    elif (p1 == 1 and p2 == 0):
        messagebox.showinfo("Notification", "Time to take Tylenol")
    else:
        messagebox.showinfo("Notification", "You have taken all of your pills for today!")

def xyz():
    ddm = d.get()
    print ("ddm: " + str(ddm))

# Dropdown Menu
d.set(options[0])
b = tk.OptionMenu(root, d, *options)

# Canvas setup #########################################################################
# Images will be placed into each
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas2 = tk.Canvas(root, width = 400, height = 300)  

# Image setup ###########################################################################
# Image 1
pillPic1 = Image.open("pill1.jpeg")
pillPic1 = pillPic1.resize((350, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
img1 = ImageTk.PhotoImage(pillPic1)
canvas1.create_image(20, 20, anchor='nw', image=img1)

# Image 2
pillPic2 = Image.open("pill2.jpeg")
pillPic2 = pillPic2.resize((250, 250), Image.ANTIALIAS) #The (250, 250) is (height, width)
img2 = ImageTk.PhotoImage(pillPic2)
canvas2.create_image(20, 20, anchor='nw', image=img2)

# Label setup ###########################################################################
myLabel1 = tk.Label(root, text="Today, March 21:")

c = tk.Label(root, text="Did you take one Warfarin pill today at 4 pm?")

# Checkbox setup ########################################################################
# Checkbox for if we have taken pill 1
myCB1 = tk.Checkbutton(root, text="Pill 1", variable=var1)

# Checkbox setup
# Checkbox for if we have taken pill 2
myCB2 = tk.Checkbutton(root, text="Pill 2", variable=var2)

# Button setup ##########################################################################
# Quits the program
myButton1 = tk.Button(root, text='Quit', command=root.quit)

# Prints 1 if we have taken a pill and 0 if we have not taken a pill
myButton2 = tk.Button(root, text='Show', command=var_states) 

# Prints the state of the dropdown menu (yes or no)
myButton0 = tk.Button(root, text="Show Selection", command=xyz) 
   

# Place everything into the grid
# row 0
myLabel1.grid(row=0, sticky='W')

# row 1
c.grid(row=1, column=0)
b.grid(row=1, column=1)

# row 2
myCB1.grid(row=2, column = 0, sticky='W')
myCB2.grid(row=2, column = 1, sticky='W')

# row 3
myButton0.grid(row=3, column=0)
myButton1.grid(row=3, column=1)
myButton2.grid(row=3, column=2) 

# row 4
canvas1.grid(row=4, column=0)
canvas2.grid(row=4, column=1)

root.mainloop()

