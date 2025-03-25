from tkinter import *
import datetime
import time
import winsound
from threading import Thread

# Create Object
root = Tk()

# Set geometry
root.geometry("400x200")

# Use Threading
def Threading():
    t1 = Thread(target=alarm)
    t1.start()

def alarm():
    set_alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    
    while True:
        # Get current time
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time, set_alarm_time)

        if current_time == set_alarm_time:
            print("Time to Wake up!")
            
            # Play beep sound 3 times
            for _ in range(3):
                winsound.Beep(1000, 1000)  # Frequency = 1000 Hz, Duration = 1000 ms
            
            break  # Stop execution after alarm triggers
        
        time.sleep(1)  # Wait for 1 second

# Add Labels, Frame, Button, Optionmenus
Label(root, text="Alarm Clock", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
Label(root, text="Set Time", font=("Helvetica 15 bold")).pack()

frame = Frame(root)
frame.pack()

hour = StringVar(root)
hours = [f"{i:02}" for i in range(24)]
hour.set(hours[0])
OptionMenu(frame, hour, *hours).pack(side=LEFT)

minute = StringVar(root)
minutes = [f"{i:02}" for i in range(60)]
minute.set(minutes[0])
OptionMenu(frame, minute, *minutes).pack(side=LEFT)

second = StringVar(root)
seconds = [f"{i:02}" for i in range(60)]
second.set(seconds[0])
OptionMenu(frame, second, *seconds).pack(side=LEFT)

Button(root, text="Set Alarm", font=("Helvetica 15"), command=Threading).pack(pady=20)

# Execute Tkinter
root.mainloop()
