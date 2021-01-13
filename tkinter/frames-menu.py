
# https://stackoverflow.com/questions/20822553/align-tabs-from-right-to-left-using-ttk-notebook-widget

import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Translator")
root.minsize(300, 300)
root.geometry("800x600")

style = ttk.Style()
style.configure('TNotebook', tabposition='nw') #'nw' as in compass direction
planner = ttk.Notebook(root, width=750, height=550)

# Create the frames of different colours that are 200*200 pixels in dimensions

tab1 = tk.Frame(planner, bg='lime green', width=300, height=300)
tab2 = tk.Frame(planner, bg='navy blue', width=300, height=300)

# Add the tabs/frames to the notebook object called "planner" 

planner.add(tab1, text='English to French')
planner.add(tab2, text='French to English')

lbl1 = tk.Label(tab1, text="Here is a Label")
lbl2 = tk.Label(tab2, text="Voici une étiquette")


def b1command():
	print ("executing b1 command")
	lbl1.configure(text="Now the label has been changed!")

def b2command():
	print ("executing b2 command")
	lbl2.configure(text="Maintenant, l'étiquette a été modifiée!")
	

b1 = tk.Button(tab1, text = "Rules", height = 5, width = 25, command = b1command)
b2 = tk.Button(tab2, text = "Règles", height = 5, width = 25, command = b2command)

planner.grid(row=0, column=0)

# Arrange everything in tab 1 
b1.grid(row=0, column=0)
lbl1.grid(row=0, column=1)

# Arrange everything in tab 2
b2.grid(row=0, column=0)
lbl2.grid(row=0, column=1)

root.mainloop()

