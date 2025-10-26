from tkinter import *

root=Tk()
root.geometry("800x600")
root.config(background="yellow")
root.title("window settings")

scroll1=Scrollbar(root)
scroll1.pack(side=LEFT,fill=Y)

list1=Listbox(root,yscrollcommand=scroll1.set)
list1.pack(side=LEFT)
list1.insert(END,"raghav")

for i in range(0,20):
    list1.insert(END,i)

scroll1.config(command=list1.yview)

root.mainloop()