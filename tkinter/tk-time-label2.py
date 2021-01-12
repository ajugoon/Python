# use Tkinter to show a digital clock
# https://www.daniweb.com/programming/software-development/code/216785/tkinter-digital-clock-python

import tkinter as tk
import time as mytime

root = tk.Tk()
root.geometry('400x300')
time1 = ''

count = 0
seconds = 50
minutes = 59
hours = 12
mm = 0


clocklbl = tk.Label(root, font=('times', 20, 'bold'), bg='green')
#clock.pack(fill=tk.BOTH, expand=1)
clocklbl.grid(column=0, row=0) #get the clock to move with resize

timerlbl = tk.Label(root, font=('times', 20, 'bold'), bg='red')
#clock.pack(fill=tk.BOTH, expand=1)
timerlbl.grid(column=0, row=1) #get the clock to move with resize

# Handles the computer clock time
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

# Handles the timer
def tock():

    global count, mm, seconds, minutes, hours

    count = (str(hours).zfill(2)+":"+str(minutes).zfill(2)+":"+str(seconds).zfill(2)+":"+str(mm))
    mm=mm+1
    mytime.sleep(0.01)
    if mm==100:
        mm=0
        seconds=seconds+1
    if seconds ==60:
        seconds=00
        minutes=minutes+1
    if minutes==60:
        minutes=00
        hours=hours+1
    if hours==13:
        hours=hours-12

    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    timerlbl.config(text=count)
    timerlbl.after(200, tock)

tick()
tock()

root.mainloop( )