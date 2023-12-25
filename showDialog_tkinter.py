from tkinter import ttk
from tkinter import *
from tools import *
form =Tk()
form.geometry("700x500")
tkcenter(form)

def f1():
    frm1= Toplevel()
    frm1.geometry("400x200")
    tkcenter(frm1)
    ttk.Button(frm1,text ="hello",command =lambda:msgbox("ok")).pack(pady=10)

    frm1.grab_set()
ttk.Button(form,text="okay",command=f1 ).pack()

form.mainloop()
