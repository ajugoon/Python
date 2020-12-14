# A simple Entry Widget example

import tkinter as tk

#Creates a window of a particular size
root = tk.Tk()
root.title("Using Frames Example")
root.geometry('800x600')

# create all of the main containers
frame0 = tk.Frame(root, 
	bg='purple',
	width=800, 
	height=100, 
	highlightbackground="black", 
	highlightthickness=2)
frame1 = tk.Frame(root, bg='blue', width=200, height=700, highlightbackground="black", highlightthickness=2)
frame2 = tk.Frame(root, bg='green', width=200, height=700, highlightbackground="black", highlightthickness=2)
frame3 = tk.Frame(root, bg='red', width=200, height=700, highlightbackground="black", highlightthickness=2)
frame4 = tk.Frame(root, bg='yellow', width=200, height=700, highlightbackground="black", highlightthickness=2)

frame0.grid(row=0, column=0, columnspan=4)
frame1.grid(row=1, column=0)
frame2.grid(row=1, column=1)
frame3.grid(row=1, column=2)
frame4.grid(row=1, column=3)


'''
# Create your frame for your buttons
frame1 = tk.Frame(root, bg="red", bd=2)
button1 = tk.Button(frame1, text="A", width = 10)
button2 = tk.Button(frame1, text="B", width = 10)
button3 = tk.Button(frame1, text="C", width = 10)
button4 = tk.Button(frame1, text="D", width = 10)
button5 = tk.Button(frame1, text="E", width = 10)

# Create a frame for your labels
frame2 = tk.Frame(root, bg="blue", bd=4)
label1 = tk.Label(frame1, bg="green", text="AAA")
label2 = tk.Label(frame1, bg="yellow", text="BBB")
label3 = tk.Label(frame1, bg="green", text="CCC")
label4 = tk.Label(frame1, bg="yellow", text="DDD")
label5 = tk.Label(frame1, bg="green", text="EEE")


frame1.grid(row=0, column=0)
button1.grid(row=1, column=0)
button2.grid(row=2, column=0)
button3.grid(row=3, column=0)
button4.grid(row=4, column=0)
button5.grid(row=5, column=0)

frame2.grid(row=0, column=1)
label1.grid(row=1, column=1)
label2.grid(row=2, column=1)
label3.grid(row=3, column=1)
label4.grid(row=4, column=1)
label5.grid(row=5, column=1)
'''

# main Loop
root.mainloop()
