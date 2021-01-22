from tkinter import *
import time

def times():
    current_time=time.strftime("%I:%M:%S:%p")
    clock_label=Label(root,text=current_time,bg='black',fg="red",font="berlin 30")
    clock_label.after(1000,times)
    clock_label.grid(row=0,column=1)

root=Tk()
root.title("Digital_Clock")
root.resizable(False,False)
times()
root.mainloop()

