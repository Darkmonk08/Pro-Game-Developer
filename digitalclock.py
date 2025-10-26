from tkinter import *
from time import strftime

root =Tk()
root.title("Clock")
root.configure(bg="white")

label1=Label(root)
label1.pack(side=BOTTOM)

label2=Label(root)
label2.pack(side=TOP)

def gettime():
    currenttime=strftime("%I:%M:%S %p")
    label1.config(text=currenttime)
    label1.after(1000,gettime)
    currentdate=strftime("%d/%m/%Y")
    label2.config(text=currentdate)
    label2.after(1000,gettime)



gettime()

root.mainloop()