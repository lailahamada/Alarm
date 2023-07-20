from tkinter import *
import datetime
import time
import winsound

def set_alarm():
    alarm_time = entry.get()
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
       
       
        if current_time == alarm_time:
            time_format.config(text="Wake up!")
           
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time_format .config(text="Alarm set for " + alarm_time)
        time.sleep(1) 

window = Tk()
window.title("Alarm Clock")

label = Label(window, text="Enter the alarm time (HH:MM:SS):")
label.pack()

entry = Entry(window)
entry.pack()

button = Button(window, text="Set Alarm", command=set_alarm)
button.pack()

time_format = Label(window, text="")
time_format .pack()


window.mainloop() 