# use Tkinter to show a digital clock
# https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python

import tkinter as tk
import time as mytime

root = tk.Tk()
time1 = ''
clocklbl = tk.Label(root, font=('times', 20, 'bold'), bg='green')
#clock.pack(fill=tk.BOTH, expand=1)
clocklbl.grid(column=0, row=0) #get the clock to move with resize

def tick():
    global time1
    # get the current local time from the PC
    time2 = mytime.strftime('%H:%M:%S')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        clocklbl.config(text=time2)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    clocklbl.after(200, tick)

tick()
root.mainloop( )