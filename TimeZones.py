from tkinter import *
##from tkmacosx import *
import pytz
from datetime import datetime
from tkinter import messagebox
import random


root=Tk()                   
root.title("Radek's Time Calculator!")
now1=StringVar()
now2=StringVar()
now3=StringVar()
now4=StringVar()


timezone1=pytz.timezone('US/Pacific')
timezone2=pytz.timezone('Europe/Madrid')
timezone3=pytz.timezone('Asia/Ho_Chi_Minh')

now1.set(datetime.now())
now2.set(datetime.now(timezone1))
now3.set(datetime.now(timezone2))
now4.set(datetime.now(timezone3))

frame1=Frame(root, width=150, height=150, bg='white')
frame2=Frame(root, width=150, height=150, bg='red')
frame3=Frame(root, width=150, height=150, bg='blue')
frame4=Frame(root, width=150, height=150, bg='red')
frame5=Frame(root, width=350, height=150, bg='red')
frame6=Frame(root, width=350, height=150, bg='orange')
frame7=Frame(root, width=350, height=150, bg='white')
frame8=Frame(root, width=350, height=150, bg='yellow')

label1=Label (frame1,height=2, text='Poland')
label2=Label (frame2,height=2, text='Spain')
label3=Label (frame3,height=2, text='Pacific Standard Time')
label4=Label (frame4,height=2, text='Vietnam')
label5=Label (frame5,height=2, textvariable=now1)
label6=Label (frame6,height=2, textvariable=now2)
label7=Label (frame7,height=2, textvariable=now3)
label8=Label (frame8,height=2, textvariable=now4)

frame1.grid(row=0,column=0)
frame2.grid(row=1,column=0)
frame3.grid(row=2,column=0)
frame4.grid(row=3,column=0)
frame5.grid(row=0,column=1)
frame6.grid(row=1,column=1)
frame7.grid(row=2,column=1)
frame8.grid(row=3,column=1)

label1.pack()
label2.pack()
label3.pack()
label4.pack()
label5.pack()
label6.pack()
label7.pack()
label8.pack()
while True:
    now1.set(datetime.now().strftime("%Y-%m-%d %I:%M:%S %p %Z"))
    now2.set(datetime.now(timezone1).strftime("%Y-%m-%d %I:%M:%S %p %Z"))
    now3.set(datetime.now(timezone2).strftime("%Y-%m-%d %I:%M:%S %p %Z"))
    now4.set(datetime.now(timezone3).strftime("%Y-%m-%d %I:%M:%S %p %Z"))

    root.update()
root.mainloop()
