from tkinter import *
from tkinter import messagebox

root=Tk()
root.geometry("800x600")
root.config(background="yellow")
root.title("window settings")

messagebox.showinfo("confirmation","image unavailable")

messagebox.showerror("error", "incorrect image format")

messagebox.showwarning("warning","image may be malicious")

print(messagebox.askquestion("close", "Are you sure you want to close the application"))

print(messagebox.askokcancel("okcancel", "cancel?"))

print(messagebox.askyesno("yesno", "yes"))

print(messagebox.askretrycancel("retry", "retry?"))

root.mainloop()
