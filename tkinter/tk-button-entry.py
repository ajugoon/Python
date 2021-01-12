import tkinter as tk


root = tk.Tk()
root.title("My TKinter Program")
root.minsize(300, 300) # height and width in pixels
root.geometry ("800x700")

def getInformation():
    print ("getting information from entry box")
    taskLabel.configure(text= "Today's Task is: " + myTask.get())

# Create your canvas/frame as needed into which the image will be placed
myFrame = tk.Frame(root, bg="lightblue", height=400, width=300)

# Create your buttons
# Note the height and the width are set in "units of text"

getButton = tk.Button(myFrame, text = "GetInfo", height = 10, width = 10, command = getInformation)

# Create your "Label"

entryLabel = tk.Label(myFrame, text="Data: ")
taskLabel = tk.Label(myFrame, text="")

# Create your "Entrybox" for input (which needs a "stringvar" to work)

myTask = tk.StringVar() # This will hold the information that is typed into the entry box
taskEntryBox = tk.Entry(myFrame, width = 15, textvariable = myTask)


# Position everything using the Grid Layout Manager
# myFrame and getButton are the only widgets being placed in "root"

getButton.grid(row=0, column=0)
myFrame.grid(row=0, column=1, columnspan=2)

# Position the labels and the entry within the "myFrame" frame

entryLabel.grid(row=1, column=0)
taskEntryBox.grid(row=2, column=1)
taskLabel.grid(row=1, column=0)

root.mainloop()




