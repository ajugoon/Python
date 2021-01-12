# use Tkinter to show a digital clock
# https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python

import tkinter as tk

root = tk.Tk()
root.geometry('400x300')

count = 0

# Handles the timer
def counter():
    global count
    count = count + 1
    timerlbl.config(text=count)
    timerlbl.after(200, counter)

def removeLabel():
    timerlbl.grid_forget()  
    # timerlbl.destroy()   # this will totally kill the label so it cannot be restored 

def showLabel():
    timerlbl.grid()   


button1 = tk.Button(root, text="Remove Label", command = removeLabel)
button2 = tk.Button(root, text="Show Label", command = showLabel)
timerlbl = tk.Label(root, font=('times', 20, 'bold'), bg='red')

button1.grid(column=0, row=0)
button2.grid(column=1, row=0)
timerlbl.grid(column=0, row=1) #get the clock to move with resize

counter()

root.mainloop( )