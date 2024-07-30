from tkinter import *
import tkinter as tk
import os
from tkinter import messagebox
from PIL import ImageTk, Image

window=Tk()
window.title("Login")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-1200
h=window.winfo_screenheight()-600
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

window.maxsize(1000,800)
window.minsize(400,200)

bg=ImageTk.PhotoImage(file="Image\\Login.jpg")
bgl=Label(window,image=bg)
bgl.place(x=0,y=0)

def verify():
    user=name.get()
    passw=psw.get()

    if user=="Om" and passw=="abcd":
        messagebox.showinfo("PASSWORD VERIFICATION", "You are login to account")
        window.destroy()
        os.system('DashBoard.py')
    else:
        messagebox.showinfo("PASSWORD VERIFICATION", "Invalid User name or password")
        var1.set('')
        var2.set('')
        name.focus_set()
        
l1=Label(window,text="LOGIN ACCOUNT",font=("comic sans ms",18,"bold"))    
l1.place(x=100,y=10)

#label
nameL=Label(window,text="Username:",width=0,height=0,font=("comic sans ms",15,"bold"))
nameL.config(bg="lightblue",fg="black")
nameL.place(x=50,y=80)

passL=Label(window,text="Password :",width=0,height=0,font=("comic sans ms",15,"bold"))
passL.config(bg="lightblue",fg="black")
passL.place(x=50,y=120)

#entry
var1=StringVar()
name=Entry(window,textvariable=var1,width=10,font=("comic sans ms",12,"bold"))
name.config(bg="white",fg="black")
name.place(x=220,y=85)

var2=StringVar()
psw=Entry(window,textvariable=var2,show="*",width=10,font=("comic sans ms",12,"bold"))
psw.config(bg="white",fg="black")
psw.place(x=220,y=125)

#button
ok=Button(window,text="LOGIN",width=0,height=0,font=("comic sans ms",10,"bold"),command=verify)
ok.config(bg="white",fg="black")
ok.place(x=120,y=200)

can=Button(window,text="CANCEL",width=0,height=0,font=("comic sans ms",10,"bold"),command=quit)
can.config(bg="white",fg="black")
can.place(x=220,y=200)

window.mainloop()
