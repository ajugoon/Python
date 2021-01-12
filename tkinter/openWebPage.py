import tkinter as tk
import webbrowser

myWindow = tk.Tk()
myWindow.title("My Music")
myWindow.geometry("4000x3000")
myWindow.configure(background="skyblue")

# Define all of your functions here (near the top of the program)

def openSpotify():
    print ("opening Spotify")
    webbrowser.open("https://www.spotify.com/ca-en/")

# Create your widgets here
# Note the height and the width are set in "units of text"

# Create button
myButton1 = tk.Button(myWindow, text = "Open Spotify", height = 10, width = 10, command = openSpotify)

#Create Label
myLabel1 = tk.Label(myWindow, text="Welcome to Smart Music", bg="skyblue", font="none 64 bold")


# Place everything into the grid

myLabel1.grid(row=0, column=0)
myButton1.grid(row=2, column=0)


myWindow.mainloop()
