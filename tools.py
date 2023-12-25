from tkinter import ttk
from tkinter import messagebox
def tkcenter(form):
    form.update()
    fw = form.winfo_width()
    fh =form.winfo_height()
    sw =form.winfo_screenwidth()
    sh =form.winfo_screenheight()
    x =(sw-fw) / 2
    y =(sh - fh) / 2 
    form.geometry("%dx%d+%d+%d" %(fw,fh,x,y))

def bgall(form,bg):
    form.update()
    ctrls = form.winfo_children()
    form.config(bg=bg)
    for c in ctrls:
        ci = c.winfo_class()
        if ci =="Label" or ci =="Button" or ci =="Entry":
            c["bg"]=bg 
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry":
            my = ttk.Style()
            my.configure("TLabel",background =bg)
            my.configure("TButton",background =bg)
            my.configure("TEntry",background =bg)
def fontall(form, font):
    form.update()
    ctrls = form.winfo_children()
    for c in ctrls:
        ci = c.winfo_class()
        
        if ci =="Label" or ci =="Button" or ci =="Entry":
            c["font"] = font
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry":
             my =ttk.Style()
             
             my.configure("TLabel",font =font)
             
             my.configure("TButton",font =font)
             
             my.configure("TEntry",font =font)

def fgall(form,fg):
    form.update()
    ctrls=form.winfo_children()
    for c in ctrls:
        ci =c.winfo_class()
        if ci =="Label" or ci =="Button" or ci =="Entry":
            c["fg"]=fg
        if ci =="TLabel" or ci =="TButton" or ci =="TEntry":
            my =ttk.Style()
            my.configure("TLabel",foreground =fg)
            my.configure("TEntry",foreground =fg)
            my.configure("TButton",foreground =fg)
def msgbox(text):
    messagebox.showinfo("",text)
    
def msgask(text):
    return messagebox.askyesno("",text)

    
