from tkinter import *
import time
root = Tk()
time1 = ''
clock = Label(root, font=('times', 100, 'bold','italic'), bg='black', fg='green')
clock.pack(fill='both', expand=1)
root.title('Digital Clock')
def tick():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(200, tick)
tick()
root.mainloop(  )

